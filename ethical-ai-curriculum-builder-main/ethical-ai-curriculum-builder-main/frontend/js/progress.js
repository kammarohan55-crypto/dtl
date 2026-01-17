function getCompletedModules(topic, level) {
  const key = `completed_${topic}_${level}`;
  return JSON.parse(localStorage.getItem(key)) || [];
}

function markModuleCompleted(topic, level, moduleName) {
  const key = `completed_${topic}_${level}`;
  let completed = getCompletedModules(topic, level);

  if (!completed.includes(moduleName)) {
    completed.push(moduleName);
    localStorage.setItem(key, JSON.stringify(completed));
  }
}

function updateProgressBar(totalModules) {
  const topic = localStorage.getItem("selectedTopic");
  const level = localStorage.getItem("selectedLevel");
  const completed = getCompletedModules(topic, level);

  const percent = totalModules === 0
    ? 0
    : Math.round((completed.length / totalModules) * 100);

  document.getElementById("progressBar").style.width = percent + "%";
}
