// AI Module Summarization Logic
// Handles API calls - ONLY on button click

document.addEventListener('DOMContentLoaded', () => {
    const summarizeBtn = document.getElementById('summarizeBtn');
    const closeSummary = document.getElementById('closeSummary');

    if (summarizeBtn) {
        summarizeBtn.addEventListener('click', handleSummarize);
    }

    if (closeSummary) {
        closeSummary.addEventListener('click', () => {
            document.getElementById('summaryContainer').style.display = 'none';
        });
    }
});

async function handleSummarize() {
    // Get state from shared moduleState
    const moduleState = window.moduleState;
    if (!moduleState) return;

    const currentModule = moduleState.getCurrentModule();
    if (!currentModule) {
        alert('Please load a module first!');
        return;
    }

    const startBtn = document.getElementById('summarizeBtn');
    const spinner = document.getElementById('loadingSpinner');
    const container = document.getElementById('summaryContainer');
    const content = document.getElementById('summaryContent');

    // UI State: Loading
    startBtn.disabled = true;
    startBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing Content...';
    spinner.style.display = 'block';
    container.style.display = 'none';

    try {
        const response = await fetch(`${moduleState.API_BASE_URL}/summarize`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                subject: currentModule.subject,
                module_id: currentModule.module_id,
                level: currentModule.level
            })
        });

        const data = await response.json();

        if (data.success) {
            displaySummary(data.summary);
            container.style.display = 'block';
            container.scrollIntoView({ behavior: 'smooth' });
        } else {
            alert('Error: ' + (data.error || 'Failed to generate summary'));
        }

    } catch (error) {
        console.error("Summarization error:", error);
        alert('Failed to connect to AI service. Ensure backend is running.');
    } finally {
        startBtn.disabled = false;
        startBtn.innerHTML = '<i class="fas fa-magic"></i> Summarize This Module with AI';
        spinner.style.display = 'none';
    }
}

function displaySummary(summary) {
    const html = `
        <div class="summary-section">
            <h4><i class="fas fa-align-left"></i> Summary</h4>
            <div class="summary-text">${summary.module_summary}</div>
        </div>
        
        ${renderListSection('key', 'Key Concepts', summary.key_concepts)}
        ${renderSection('lightbulb', 'Intuition', summary.intuition)}
        ${renderExamples(summary.worked_examples)}
        ${renderListSection('exclamation-triangle', 'Common Mistakes', summary.common_mistakes)}
        ${renderListSection('graduation-cap', 'Exam Takeaways', summary.exam_takeaways)}
        ${renderListSection('globe', 'Real-World Applications', summary.real_world_applications)}
    `;

    document.getElementById('summaryContent').innerHTML = html;
}

function renderSection(icon, title, content) {
    if (!content) return '';
    return `
        <div class="summary-section">
            <h4><i class="fas fa-${icon}"></i> ${title}</h4>
            <div class="summary-text">${content}</div>
        </div>
    `;
}

function renderListSection(icon, title, list) {
    if (!list || list.length === 0) return '';
    return `
        <div class="summary-section">
            <h4><i class="fas fa-${icon}"></i> ${title}</h4>
            <ul class="summary-list">
                ${list.map(item => `<li>${item}</li>`).join('')}
            </ul>
        </div>
    `;
}

function renderExamples(examples) {
    if (!examples || examples.length === 0) return '';
    // Actually, summary examples are redundant if module has them, but user asked for summary.
    // We'll show them concisely.
    return `
       <div class="summary-section">
           <h4><i class="fas fa-pencil-ruler"></i> AI Examples</h4>
           ${examples.map((ex, i) => `
               <div class="example-card-summary">
                   <strong>Ex ${i + 1}:</strong> ${ex.problem}<br>
                   <em>Sol:</em> ${ex.solution.substring(0, 100)}...
               </div>
           `).join('')}
       </div>
    `;
}
