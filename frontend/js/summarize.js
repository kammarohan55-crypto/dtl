// AI Module Summarization - Works with NEW JSON schema
// Displays ai_summary from module data (no backend API needed)

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
    const moduleState = window.moduleState;
    if (!moduleState) return;

    const currentModule = moduleState.getCurrentModule();
    if (!currentModule || !currentModule.data) {
        alert('Please load a module first!');
        return;
    }

    const aiSummary = currentModule.data.ai_summary;

    if (!aiSummary) {
        alert('No AI summary available for this module.');
        return;
    }

    const startBtn = document.getElementById('summarizeBtn');
    const container = document.getElementById('summaryContainer');

    // UI State: Loading
    startBtn.disabled = true;
    startBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading Summary...';

    // Small delay for UX effect
    setTimeout(() => {
        displaySummary(aiSummary);
        container.style.display = 'block';
        container.scrollIntoView({ behavior: 'smooth' });

        startBtn.disabled = false;
        startBtn.innerHTML = '<i class="fas fa-sparkles"></i> AI Summary';

        // Trigger MathJax for formulas in summary
        if (window.MathJax) {
            window.MathJax.typesetPromise();
        }
    }, 500);
}

function displaySummary(summary) {
    // NEW schema: ai_summary has:
    // - key_ideas (array)
    // - important_formulas (array)
    // - common_exam_traps (array)
    // - exam_tip (string)

    let html = '';

    // Key Ideas
    if (summary.key_ideas && summary.key_ideas.length > 0) {
        html += `
            <div class="summary-section">
                <h4><i class="fas fa-lightbulb"></i> Key Ideas</h4>
                <ul class="summary-list">
                    ${summary.key_ideas.map(idea => `<li>${idea}</li>`).join('')}
                </ul>
            </div>
        `;
    }

    // Important Formulas
    if (summary.important_formulas && summary.important_formulas.length > 0) {
        html += `
            <div class="summary-section">
                <h4><i class="fas fa-square-root-alt"></i> Important Formulas</h4>
                <ul class="summary-list formula-list">
                    ${summary.important_formulas.map(formula => `<li>${formula}</li>`).join('')}
                </ul>
            </div>
        `;
    }

    // Common Exam Traps
    if (summary.common_exam_traps && summary.common_exam_traps.length > 0) {
        html += `
            <div class="summary-section">
                <h4><i class="fas fa-exclamation-triangle"></i> Common Exam Traps</h4>
                <ul class="summary-list">
                    ${summary.common_exam_traps.map(trap => `<li>${trap}</li>`).join('')}
                </ul>
            </div>
        `;
    }

    // Exam Tip
    if (summary.exam_tip) {
        html += `
            <div class="summary-section">
                <h4><i class="fas fa-graduation-cap"></i> Exam Tip</h4>
                <div class="summary-text exam-tip-box">
                    ${summary.exam_tip}
                </div>
            </div>
        `;
    }

    // Fallback if no content
    if (!html) {
        html = '<p>No summary content available for this module.</p>';
    }

    document.getElementById('summaryContent').innerHTML = html;
}
