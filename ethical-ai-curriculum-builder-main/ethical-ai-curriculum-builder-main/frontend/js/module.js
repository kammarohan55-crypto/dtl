const topic = localStorage.getItem("selectedTopic");
const level = localStorage.getItem("selectedLevel");
const moduleName = localStorage.getItem("selectedModule");

if (!topic || !level || !moduleName) {
  alert("Missing module data");
  window.location.href = "index.html";
}

const titleEl = document.getElementById("moduleTitle");
const contentEl = document.getElementById("moduleContent");
const insightEl = document.getElementById("industryInsight");
const completeBtn = document.getElementById("completeBtn");

fetch(`http://127.0.0.1:8000/module/${topic}/${level}/${moduleName}`)
  .then(res => res.json())
  .then(data => {
    titleEl.textContent = data.title;

    data.content.forEach(para => {
      const p = document.createElement("p");
      p.textContent = para;
      contentEl.appendChild(p);
    });

    if (data.industry_insight) {
      insightEl.innerHTML = `<strong>Industry Insight:</strong> ${data.industry_insight}`;
    }

    fetch(`http://127.0.0.1:8000/modules/${topic}/${level}`)
      .then(res => res.json())
      .then(modData => updateProgressBar(modData.modules.length));
  });

completeBtn.addEventListener("click", () => {
  markModuleCompleted(topic, level, moduleName);

  fetch(`http://127.0.0.1:8000/modules/${topic}/${level}`)
    .then(res => res.json())
    .then(modData => updateProgressBar(modData.modules.length));

  alert("Module marked as completed!");
});
document.getElementById("quizBtn").onclick = () => {
  window.location.href = "quiz.html";
};
