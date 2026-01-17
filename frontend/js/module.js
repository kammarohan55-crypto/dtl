// Module Loading Logic - Linked to Roadmap
const API_BASE_URL = 'http://localhost:5000/api';

// State
let currentModule = null;

document.addEventListener('DOMContentLoaded', () => {
    initModule();
});

async function initModule() {
    // 1. Check LocalStorage for valid state
    const subject = localStorage.getItem('selectedSubject');
    const level = localStorage.getItem('selectedLevel');
    const moduleId = localStorage.getItem('selectedModuleId');

    if (!subject || !level || !moduleId) {
        alert("No module selected. Redirecting to Roadmap.");
        window.location.href = 'roadmap.html';
        return;
    }

    // 2. Load the Module Data
    try {
        const response = await fetch(`${subject}_curriculum.json`);
        if (!response.ok) throw new Error("Failed to fetch curriculum");

        const data = await response.json();

        // Find the module
        const moduleList = data.levels[level].modules;
        const module = moduleList.find(m => m.module_id === moduleId);

        if (!module) throw new Error("Module not found in curriculum");

        currentModule = { ...module, subject, level };

        // 3. Render Module
        renderModule(currentModule);

    } catch (err) {
        console.error(err);
        document.getElementById('moduleName').textContent = "Error Loading Module";
        document.getElementById('moduleContent').innerHTML = `<p class="error">Failed to load content: ${err.message}. <a href="roadmap.html">Back</a></p>`;
        document.getElementById('moduleContent').style.display = 'block';
    }
}

function renderModule(module) {
    document.getElementById('moduleName').textContent = module.module_name;
    document.getElementById('moduleLevelBadge').textContent = module.level;

    const cards = module.content_cards;

    // 1. Motivation
    document.getElementById('moduleMotivation').textContent = cards.motivation ? cards.motivation.content : "Master this concept to unlock advanced applications.";

    // 2. Concept Overview (List)
    const conceptDiv = document.getElementById('conceptContent');
    const points = cards.concept_overview ? cards.concept_overview.points : ["Core fundamental topic."];
    conceptDiv.innerHTML = `<ul>${points.map(p => `<li>${p}</li>`).join('')}</ul>`;

    // 3. Intuition (Rich Text)
    document.getElementById('intuitionContent').innerHTML = formatText(cards.intuition ? cards.intuition.content : module.core_content.intuition);

    // 4. Mathematical Formulation (LaTeX)
    document.getElementById('mathContent').innerHTML = formatText(cards.math_derivation ? cards.math_derivation.content : "No formulation required.");

    // 5. Worked Example (Rich Text)
    const exDiv = document.getElementById('exampleContent');
    if (cards.worked_example) {
        exDiv.innerHTML = `
            <div class="problem"><strong>Q:</strong> ${formatText(cards.worked_example.problem)}</div>
            <div class="solution"><strong>A:</strong> ${formatText(cards.worked_example.solution)}</div>
        `;
    } else {
        exDiv.innerHTML = "No example provided.";
    }

    // 6. Takeaways (List)
    const takeDiv = document.getElementById('takeawaysContent');
    const takeaways = cards.key_takeaways ? cards.key_takeaways.points : [];
    takeDiv.innerHTML = `<ul>${takeaways.map(t => `<li>${t}</li>`).join('')}</ul>`;

    // Show Content
    document.getElementById('moduleContent').style.display = 'block';

    // TRIGGER MATHJAX
    if (window.MathJax) {
        window.MathJax.typesetPromise();
    }
}

function formatText(text) {
    if (!text) return '';
    // Basic formatting: newlines to <br>, bold to <strong>
    let html = text
        .replace(/\n\n/g, '<br><br>')
        .replace(/\n/g, '<br>')
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

    // Handle code blocks (simple regex for MVP)
    if (html.includes('```')) {
        html = html.replace(/```(.*?)```/gs, '<pre><code>$1</code></pre>');
    }
    return html;
}

// Export state
window.moduleState = {
    getCurrentModule: () => currentModule,
    API_BASE_URL
};
