const highScoreElement = document.querySelector(".high-score");
let highScore = localStorage.getItem("high-score") || 0;
highScoreElement.innerText = `${highScore}`;