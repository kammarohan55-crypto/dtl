const topic = localStorage.getItem("selectedTopic");
const level = localStorage.getItem("selectedLevel");

let difficulty = level === "beginner" ? "easy"
               : level === "intermediate" ? "medium"
               : "hard";

let questions = [];
let index = 0;
let score = 0;

fetch(`http://127.0.0.1:8000/quizzes/${topic}/${level}`)
  .then(res => res.json())
  .then(data => {
    questions = data[difficulty].slice(0, 5);
    showQuestion();
  });

function showQuestion() {
  if (index >= questions.length) {
    finishQuiz();
    return;
  }

  const q = questions[index];
  const box = document.getElementById("questionBox");

  box.innerHTML = `
    <p>${q.question}</p>
    ${q.options.map(opt =>
      `<label>
         <input type="radio" name="opt" value="${opt}"> ${opt}
       </label><br>`
    ).join("")}
  `;
}

document.getElementById("nextBtn").onclick = () => {
  const selected = document.querySelector("input[name='opt']:checked");
  if (!selected) return alert("Select an option");

  if (selected.value === questions[index].answer) {
    score++;
  }

  index++;
  showQuestion();
};

function finishQuiz() {
  const percent = (score / questions.length) * 100;

  let msg = `Score: ${score}/${questions.length}`;

  if (percent >= 80) {
    msg += "\nDifficulty increased next time!";
  } else if (percent < 50) {
    msg += "\nDifficulty will be reduced next time.";
  }

  alert(msg);
  window.location.href = "module.html";
}
