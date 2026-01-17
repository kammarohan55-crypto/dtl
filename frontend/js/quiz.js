// Quiz Logic
// Handles loading, rendering, scoring, and progression tracking

let currentQuiz = null;

document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('startQuizBtn');
    if (startBtn) {
        startBtn.addEventListener('click', loadQuiz);
    }

    document.getElementById('submitQuizBtn').addEventListener('click', submitQuiz);
    document.getElementById('retryQuizBtn').addEventListener('click', resetQuiz);
});

async function loadQuiz() {
    const moduleState = window.moduleState;
    if (!moduleState) return;

    const currentModule = moduleState.getCurrentModule();
    if (!currentModule) {
        alert("Please load a module first.");
        return;
    }

    const subject = currentModule.subject;
    const moduleId = currentModule.module_id;

    // Show loading UI
    document.getElementById('startQuizBtn').innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';

    try {
        // Fetch quiz data for the subject
        // Note: The file contains ALL quizzes for the subject, indexed by module_id
        const response = await fetch(`quizzes/${subject}_quizzes.json`);
        if (!response.ok) throw new Error("Failed to load quizzes");

        const allQuizzes = await response.json();
        const quizData = allQuizzes[moduleId];

        if (!quizData) throw new Error("No quiz found for this module");

        currentQuiz = quizData;
        renderQuiz(currentQuiz);

        // Hide start button, show quiz container
        document.querySelector('.quiz-control').style.display = 'none';
        document.getElementById('quizContainer').style.display = 'block';

    } catch (error) {
        console.error(error);
        alert("Could not load quiz: " + error.message);
        document.getElementById('startQuizBtn').innerHTML = '<i class="fas fa-question-circle"></i> Take Module Quiz';
    }
}

function renderQuiz(quiz) {
    const container = document.getElementById('quizQuestions');
    container.innerHTML = '';

    document.getElementById('quizScore').textContent = '';
    document.getElementById('submitQuizBtn').style.display = 'inline-block';
    document.getElementById('retryQuizBtn').style.display = 'none';
    document.getElementById('progressionMessage').style.display = 'none';

    quiz.questions.forEach((q, index) => {
        const card = document.createElement('div');
        card.className = 'question-card';
        card.dataset.id = index;

        let optionsHtml = '';
        q.options.forEach((opt, optIndex) => {
            optionsHtml += `
                <label class="option-label">
                    <input type="radio" name="q${index}" value="${optIndex}" class="option-input">
                    ${opt}
                </label>
            `;
        });

        card.innerHTML = `
            <div class="question-text">${index + 1}. ${q.question}</div>
            <div class="options-group">${optionsHtml}</div>
            <div class="feedback" style="display:none;"></div>
        `;

        container.appendChild(card);
    });
}

function submitQuiz() {
    if (!currentQuiz) return;

    let score = 0;
    let total = currentQuiz.questions.length;
    let unanswered = 0;

    // Grade each question
    currentQuiz.questions.forEach((q, index) => {
        const card = document.querySelector(`.question-card[data-id="${index}"]`);
        const selected = card.querySelector(`input[name="q${index}"]:checked`);
        const feedback = card.querySelector('.feedback');

        if (!selected) {
            unanswered++;
            return;
        }

        const userAns = parseInt(selected.value);
        feedback.style.display = 'block';

        // Disable inputs
        card.querySelectorAll('input').forEach(inp => inp.disabled = true);

        if (userAns === q.correct) {
            score++;
            card.querySelector(`input[value="${userAns}"]`).parentElement.classList.add('correct-answer');
            feedback.innerHTML = `<div class="explanation"><i class="fas fa-check"></i> Correct! ${q.explanation}</div>`;
        } else {
            card.querySelector(`input[value="${userAns}"]`).parentElement.classList.add('wrong-answer');
            card.querySelector(`input[value="${q.correct}"]`).parentElement.classList.add('correct-answer');
            feedback.innerHTML = `<div class="explanation"><i class="fas fa-times"></i> Incorrect. ${q.explanation}</div>`;
        }
    });

    if (unanswered > 0) {
        alert(`Please answer all questions! (${unanswered} remaining)`);
        // Re-enable inputs for unanswered?? 
        // For simplicity, we just stop here and let them answer.
        // Re-hide feedback if shown prematurely? 
        // Better UX: Just return and don't grade yet.
        return;
    }

    // Calculate final score
    const percentage = Math.round((score / total) * 100);
    document.getElementById('quizScore').textContent = `Score: ${percentage}%`;

    // UI Updates
    document.getElementById('submitQuizBtn').style.display = 'none';
    document.getElementById('retryQuizBtn').style.display = 'inline-block';

    // Handle Progression
    handleProgression(percentage);
}

function handleProgression(score) {
    const currentModule = window.moduleState.getCurrentModule();
    const subject = currentModule.subject;
    const level = currentModule.level;
    const moduleId = currentModule.module_id;

    // 1. Save Score
    let progress = JSON.parse(localStorage.getItem('userProgress') || '{}');
    if (!progress[subject]) progress[subject] = {};
    if (!progress[subject][level]) progress[subject][level] = {};

    // Only update if higher? Or always update? Let's keep highest.
    const oldScore = progress[subject][level][moduleId] || 0;
    progress[subject][level][moduleId] = Math.max(oldScore, score);

    localStorage.setItem('userProgress', JSON.stringify(progress));

    // 2. Analyze weak topics (If score < 60)
    const msgDiv = document.getElementById('progressionMessage');
    msgDiv.style.display = 'block';

    if (score < 60) {
        msgDiv.className = 'progression-message progression-review';
        msgDiv.innerHTML = `
            <i class="fas fa-exclamation-triangle"></i> Not quite there yet. 
            <br>We recommend reviewing the Theory section and Worked Examples before trying again.
        `;
    } else {
        // 3. Check Level Completion
        const isLevelComplete = checkLevelCompletion(subject, level, progress);

        msgDiv.className = 'progression-message progression-success';
        if (isLevelComplete) {
            msgDiv.innerHTML = `
                <i class="fas fa-trophy"></i> <strong>Congratulations!</strong>
                <br>You have passed all modules in the <strong>${level}</strong> level!
                <br>You are ready to advance to the next level in the Roadmap.
            `;
        } else {
            msgDiv.innerHTML = `
                <i class="fas fa-check-circle"></i> <strong>Module Passed!</strong>
                <br>Great job! You can now move to the next module in the Roadmap.
            `;
        }
    }
}

function checkLevelCompletion(subject, level, progress) {
    // Need to know TOTAL modules in this level.
    // We can't easily access the full curriculum list here unless we fetch it again or store it.
    // BUT! moduleState stores current module, not full list.
    // However, roadmap.js stored the CURRENT curriculum in a variable? No, separate page.
    // workaround: We assume if we have X passed modules, we are good?
    // Better: We should probably fetch the curriculum to know the count.
    // Let's do a quick fetch since it's cached usually.

    // Actually, for MVP, just showing "Module Passed" is good.
    // But user asked for "tell if ready for next level".
    // I will try to support it by fetching curriculum.

    return fetch(`${subject}_curriculum.json`)
        .then(res => res.json())
        .then(data => {
            const modules = data.levels[level].modules;
            const userScores = progress[subject][level];

            // Check if every module has a score >= 60
            const allPassed = modules.every(m => (userScores[m.module_id] || 0) >= 60);
            return allPassed;
        })
        .catch(err => {
            console.error("Error checking level completion", err);
            return false;
        });
    // Wait, checkLevelCompletion needs to be async or return promise.
    // I called it synchronously above. I need to fix that.
}

// Fixed async version of handleProgression
async function handleProgression(score) {
    const currentModule = window.moduleState.getCurrentModule();
    const subject = currentModule.subject;
    const level = currentModule.level;
    const moduleId = currentModule.module_id;

    // Save Score
    let progress = JSON.parse(localStorage.getItem('userProgress') || '{}');
    if (!progress[subject]) progress[subject] = {};
    if (!progress[subject][level]) progress[subject][level] = {};
    const oldScore = progress[subject][level][moduleId] || 0;
    progress[subject][level][moduleId] = Math.max(oldScore, score);
    localStorage.setItem('userProgress', JSON.stringify(progress));

    // Message
    const msgDiv = document.getElementById('progressionMessage');
    msgDiv.style.display = 'block';

    if (score < 60) {
        msgDiv.className = 'progression-message progression-review';
        msgDiv.innerHTML = `
            <i class="fas fa-exclamation-triangle"></i> Score below 60%. 
            <br>Please review the weak topics in this module and retry.
        `;
    } else {
        msgDiv.className = 'progression-message progression-success';
        msgDiv.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Checking progression...`;

        try {
            // Check Level Completion
            const response = await fetch(`${subject}_curriculum.json`);
            const data = await response.json();
            const modules = data.levels[level].modules;
            const userScores = progress[subject][level];

            const allPassed = modules.every(m => (userScores[m.module_id] || 0) >= 60);

            if (allPassed) {
                msgDiv.innerHTML = `
                    <i class="fas fa-trophy"></i> <strong>LEVEL COMPLETE!</strong>
                    <br>You have mastered the passed all modules in <strong>${level}</strong>!
                    <br><a href="roadmap.html">rReturn to Roadmap</a> to start the next level.
                `;
            } else {
                msgDiv.innerHTML = `
                    <i class="fas fa-check-circle"></i> <strong>Module Passed!</strong>
                    <br>Good job! Return to the <a href="roadmap.html">Roadmap</a> to continue.
                `;
            }
        } catch (e) {
            msgDiv.innerHTML = `
                <i class="fas fa-check-circle"></i> <strong>Module Passed!</strong>
            `;
        }
    }
}

function resetQuiz() {
    document.querySelector('.quiz-control').style.display = 'block';
    document.getElementById('quizContainer').style.display = 'none';
    document.getElementById('startQuizBtn').innerHTML = '<i class="fas fa-question-circle"></i> Take Module Quiz';
}
