const topicSelect = document.getElementById("topic");
const levelSelect = document.getElementById("level");
const startBtn = document.getElementById("startBtn");

// Fetch topics from backend
fetch("http://127.0.0.1:8000/topics")
  .then(response => response.json())
  .then(data => {
    topicSelect.innerHTML = '<option value="">Select subject</option>';
    data.topics.forEach(topic => {
      const option = document.createElement("option");
      option.value = topic;
      option.textContent = topic;
      topicSelect.appendChild(option);
    });
  })
  .catch(error => {
    console.error("Error fetching topics:", error);
    topicSelect.innerHTML = '<option>Error loading topics</option>';
  });

// Handle button click
startBtn.addEventListener("click", () => {
  const topic = topicSelect.value;
  const level = levelSelect.value;

  if (!topic || !level) {
    alert("Please select both subject and level");
    return;
  }

  // Save selection
  localStorage.setItem("selectedTopic", topic);
  localStorage.setItem("selectedLevel", level);

  // Go to roadmap page
  window.location.href = "roadmap.html";
});
