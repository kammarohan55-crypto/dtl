// Roadmap Tree Logic
// Reads directly from curriculum JSONs to ensure 100% sync with content

let currentSubject = null;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    setupSubjectSelection();
    setupBackButton();
});

function setupSubjectSelection() {
    const cards = document.querySelectorAll('.subject-card');
    cards.forEach(card => {
        card.addEventListener('click', () => {
            const subject = card.getAttribute('data-subject');
            loadSubjectTree(subject);
        });
    });
}

function setupBackButton() {
    document.getElementById('backBtn').addEventListener('click', () => {
        document.getElementById('roadmapDisplay').style.display = 'none';
        document.getElementById('subjectSelection').style.display = 'grid';
        document.querySelector('.main-header').scrollIntoView({ behavior: 'smooth' });
    });
}

async function loadSubjectTree(subject) {
    currentSubject = subject;

    // Show loading or transition?

    try {
        // Fetch the RICH CONTENT curriculum directly
        const response = await fetch(`${subject}_curriculum.json`);
        if (!response.ok) throw new Error('Failed to load curriculum');

        const data = await response.json();
        renderTree(data);

        // Switch views
        document.getElementById('subjectSelection').style.display = 'none';
        document.getElementById('roadmapDisplay').style.display = 'block';
        document.getElementById('roadmapTitle').textContent = formatSubjectName(subject) + " Roadmap";

    } catch (error) {
        console.error(error);
        alert("Error loading roadmap data. Ensure servers are running.");
    }
}

function renderTree(data) {
    const levels = ['beginner', 'intermediate', 'advanced'];

    levels.forEach(level => {
        const container = document.getElementById(`${level}Nodes`);
        container.innerHTML = ''; // Clear previous

        if (data.levels[level] && data.levels[level].modules) {
            data.levels[level].modules.forEach(mod => {
                const node = document.createElement('div');
                node.className = 'node-chip';
                // Check if completed? (Future feature: read from localStorage)
                // const isCompleted = checkCompletion(mod.module_id);
                // if (isCompleted) node.classList.add('completed');

                node.innerHTML = `<i class="fas fa-circle"></i> ${mod.module_name}`;

                node.addEventListener('click', () => {
                    goToModule(mod.module_id, level);
                });

                container.appendChild(node);
            });
        }
    });
}

function goToModule(moduleId, level) {
    // Save state so module.html knows what to load
    localStorage.setItem('selectedSubject', currentSubject);
    localStorage.setItem('selectedLevel', level);
    localStorage.setItem('selectedModuleId', moduleId);

    // Redirect
    window.location.href = 'module.html';
}

function formatSubjectName(slug) {
    if (slug === 'aiml') return 'AI & Machine Learning';
    if (slug === 'programming_c') return 'C Programming';
    return slug.charAt(0).toUpperCase() + slug.slice(1);
}
