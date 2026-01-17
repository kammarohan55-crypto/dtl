const topic = localStorage.getItem("selectedTopic");
const level = localStorage.getItem("selectedLevel");
const modulesDiv = document.getElementById("modules");
const heading = document.getElementById("heading");

if (!topic || !level) {
  alert("No topic or level selected");
  window.location.href = "index.html";
}

heading.textContent = `Roadmap: ${topic.toUpperCase()} (${level})`;

// Fetch modules from backend
fetch(`http://127.0.0.1:8000/modules/${topic}/${level}`)
  .then(response => response.json())
  .then(data => {
    modulesDiv.innerHTML = "";

    if (data.modules.length === 0) {
      modulesDiv.textContent = "No modules available.";
      return;
    }

    data.modules.forEach(module => {
      const btn = document.createElement("button");
      btn.textContent = module;
      btn.style.display = "block";
      btn.style.margin = "10px 0";

      btn.addEventListener("click", () => {
        localStorage.setItem("selectedModule", module);
        window.location.href = "module.html";
      });

      modulesDiv.appendChild(btn);
    });
  })
  .catch(err => {
    console.error(err);
    modulesDiv.textContent = "Error loading modules";
  });
