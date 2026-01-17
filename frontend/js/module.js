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

    // 2. Load the Module Data directly from the JSON file
    // We reuse the filename convention: [subject]_curriculum.json
    try {
        const response = await fetch(`${subject}_curriculum.json`);
        if (!response.ok) throw new Error("Failed to fetch curriculum");

        const data = await response.json();

        // Find the module
        const moduleList = data.levels[level].modules;
        const module = moduleList.find(m => m.module_id === moduleId);

        if (!module) throw new Error("Module not found in curriculum");

        currentModule = { ...module, subject, level }; // Enrich with context

        // 3. Render Module
        renderModule(currentModule);

    } catch (err) {
        console.error(err);
        document.getElementById('moduleName').textContent = "Error Loading Module";
        document.getElementById('moduleContent').innerHTML = `<p class="error">Failed to load content: ${err.message}. <br><a href="roadmap.html">Back to Roadmap</a></p>`;
        document.getElementById('moduleContent').style.display = 'block';
    }
}

function renderModule(module) {
    document.getElementById('moduleName').textContent = module.module_name;
    const badge = document.getElementById('moduleLevel');
    badge.textContent = module.level.toUpperCase();
    badge.className = `badge badge-${module.level}`;

    // Objectives
    const objList = document.getElementById('objectives');
    objList.innerHTML = '';
    module.learning_objectives.forEach(obj => {
        const li = document.createElement('li');
        li.textContent = obj;
        objList.appendChild(li);
    });

    // Theory
    // Simple markdown-like parser for newlines/bold
    const theoryHTML = formatText(module.core_content.theory);
    document.getElementById('theoryContent').innerHTML = theoryHTML;

    // Examples
    const exDiv = document.getElementById('examplesContent');
    exDiv.innerHTML = '';
    module.core_content.worked_examples.forEach((ex, i) => {
        const card = document.createElement('div');
        card.className = 'example-card';
        card.innerHTML = `
            <h4>Example ${i + 1}</h4>
            <div class="problem"><strong>Q:</strong> ${formatText(ex.problem)}</div>
            <div class="solution"><strong>A:</strong> ${formatText(ex.solution)}</div>
        `;
        exDiv.appendChild(card);
    });

    // Show Content
    document.getElementById('moduleContent').style.display = 'block';
}

function formatText(text) {
    if (!text) return '';
    // Basic formatting: newlines to <br>, bold to <strong>
    let html = text
        .replace(/\n\n/g, '<br><br>')
        .replace(/\n/g, '<br>')
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

    // Handle code blocks if possible (simple)
    if (html.includes('```')) {
        html = html.replace(/```(.*?)```/gs, '<pre><code>$1</code></pre>');
    }
    return html;
}

// Export state for other scripts (summarize.js, quiz.js)
window.moduleState = {
    getCurrentModule: () => currentModule,
    API_BASE_URL
};
