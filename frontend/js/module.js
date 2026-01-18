// Module Loading Logic - Works with NEW JSON schema
// Loads full module content from modules/{subject}/{level}/{module_id}.json

let currentModuleData = null;

document.addEventListener('DOMContentLoaded', () => {
    initModule();
});

async function initModule() {
    // 1. Check LocalStorage for module selection
    const subject = localStorage.getItem('selectedSubject');
    const level = localStorage.getItem('selectedLevel');
    const moduleId = localStorage.getItem('selectedModuleId');

    if (!subject || !level || !moduleId) {
        alert("No module selected. Redirecting to Roadmap.");
        window.location.href = 'roadmap.html';
        return;
    }

    // 2. Load the FULL module JSON file
    try {
        const modulePath = `../modules/${subject}/${level}/${moduleId}.json`;
        const response = await fetch(modulePath);

        if (!response.ok) throw new Error(`Failed to load module from ${modulePath}`);

        const moduleData = await response.json();
        currentModuleData = { ...moduleData, subject, level, module_id: moduleId };

        // 3. Render Module Content
        renderModule(currentModuleData);

    } catch (err) {
        console.error(err);
        document.getElementById('moduleName').textContent = "Error Loading Module";
        document.getElementById('moduleContent').innerHTML = `<p class="error">Failed to load content: ${err.message}. <a href="roadmap.html">Back</a></p>`;
        document.getElementById('moduleContent').style.display = 'block';
    }
}

function renderModule(data) {
    // Module Header
    const header = data.module_header;
    document.getElementById('moduleName').textContent = header.module_title;
    document.getElementById('moduleLevelBadge').textContent = header.level;

    // Definition as motivation
    document.getElementById('moduleMotivation').textContent = data.definition || "Master this fundamental concept.";

    // 1. Concept Overview (array of strings)
    const conceptDiv = document.getElementById('conceptContent');
    const concepts = data.concept_overview || [];
    conceptDiv.innerHTML = `<ul>${concepts.map(c => `<li>${c}</li>`).join('')}</ul>`;

    // 2. Intuition - Use THEORY section (comprehensive content)
    const theoryText = Array.isArray(data.theory) ? data.theory.join('\n\n') : data.theory || "";
    document.getElementById('intuitionContent').innerHTML = formatText(theoryText);

    // 3. Mathematical Formulation
    const mathDiv = document.getElementById('mathContent');
    if (data.mathematical_formulation && data.mathematical_formulation.length > 0) {
        let mathHtml = '';
        data.mathematical_formulation.forEach(item => {
            mathHtml += `
                <div class="formula-block">
                    <div class="formula">${item.formula}</div>
                    <div class="formula-explanation">${item.explanation}</div>
                </div>
            `;
        });
        mathDiv.innerHTML = mathHtml;
    } else {
        mathDiv.innerHTML = "<p>No mathematical formulation required for this topic.</p>";
    }

    // 4. Worked Examples
    const exDiv = document.getElementById('exampleContent');
    if (data.worked_examples && data.worked_examples.length > 0) {
        let exHtml = '';
        data.worked_examples.forEach((ex, idx) => {
            const steps = Array.isArray(ex.solution_steps) ? ex.solution_steps.join('<br>') : ex.solution_steps || "";
            exHtml += `
                <div class="example-block">
                    <div class="example-header">
                        <span class="difficulty-badge" style="background: ${getDifficultyColor(ex.difficulty)}">${ex.difficulty || 'General'}</span>
                        <strong>Example ${idx + 1}</strong>
                    </div>
                    <div class="problem"><strong>Problem:</strong> ${ex.problem}</div>
                    <div class="solution">
                        <strong>Solution:</strong><br>
                        ${formatText(steps)}
                    </div>
                    ${ex.final_answer ? `<div class="final-answer"><strong>Answer:</strong> ${ex.final_answer}</div>` : ''}
                </div>
            `;
        });
        exDiv.innerHTML = exHtml;
    } else {
        exDiv.innerHTML = "<p>No worked examples for this module.</p>";
    }

    // 5. Key Takeaways
    const takeDiv = document.getElementById('takeawaysContent');
    const takeaways = data.key_takeaways || [];
    takeDiv.innerHTML = `<ul>${takeaways.map(t => `<li>${t}</li>`).join('')}</ul>`;

    // Show Content
    document.getElementById('moduleContent').style.display = 'block';

    // TRIGGER MATHJAX rendering
    if (window.MathJax) {
        window.MathJax.typesetPromise().catch(err => console.error('MathJax error:', err));
    }
}

function formatText(text) {
    if (!text) return '';

    // Convert arrays to text
    if (Array.isArray(text)) {
        text = text.join('\n\n');
    }

    // Basic formatting: newlines to <br>, bold markdown to <strong>
    let html = text
        .replace(/\n\n/g, '<br><br>')
        .replace(/\n/g, '<br>')
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

    // Handle code blocks
    if (html.includes('```')) {
        html = html.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
    }

    return html;
}

function getDifficultyColor(difficulty) {
    if (!difficulty) return '#6b7280';
    if (difficulty.toLowerCase().includes('basic') || difficulty.toLowerCase().includes('easy')) return '#10b981';
    if (difficulty.toLowerCase().includes('intermediate') || difficulty.toLowerCase().includes('medium')) return '#f59e0b';
    if (difficulty.toLowerCase().includes('advanced') || difficulty.toLowerCase().includes('hard')) return '#ef4444';
    return '#6b7280';
}

// Export state for quiz and summary
window.moduleState = {
    getCurrentModule: () => {
        if (!currentModuleData) return null;
        return {
            subject: currentModuleData.subject,
            level: currentModuleData.level,
            module_id: currentModuleData.module_id,
            module_name: currentModuleData.module_header?.module_title || 'Unknown',
            data: currentModuleData  // Full module data for quiz/summary
        };
    }
};
