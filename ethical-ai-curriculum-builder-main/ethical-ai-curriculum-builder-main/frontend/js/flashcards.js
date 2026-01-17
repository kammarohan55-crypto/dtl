const topic = localStorage.getItem("selectedTopic");
const level = localStorage.getItem("selectedLevel");

const flashBtn = document.getElementById("flashcardBtn");

flashBtn.addEventListener("click", () => {
  fetch(`http://127.0.0.1:8000/flashcards/${topic}/${level}`)
    .then(res => res.json())
    .then(cards => {
      let index = 0;
      showCard(cards[index]);

      function showCard(card) {
        const box = document.createElement("div");
        box.innerHTML = `
          <h4>${card.front}</h4>
          <p>${card.back}</p>
          <button id="nextCard">Next</button>
        `;
        document.body.appendChild(box);

        document.getElementById("nextCard").onclick = () => {
          document.body.removeChild(box);
          index = (index + 1) % cards.length;
          showCard(cards[index]);
        };
      }
    });
});
