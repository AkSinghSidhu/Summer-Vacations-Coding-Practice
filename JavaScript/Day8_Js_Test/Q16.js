// HTML has a table: 3 columns (Name, Score, Status), 5 hardcoded rows. JS: read all scores, calculate average, highlight rows above average by changing background color, add a final summary row at the bottom: `"Class Average: 82.4"`. All done via JS — don't touch the HTML after writing it.

const scoreTable = document.querySelectorAll("table tr");
const table = document.querySelector("table");
let sum = 0;

for (let i = 1; i < scoreTable.length; i++){
    sum = sum + parseInt(scoreTable[i].cells[1].textContent);
}

const average = sum / (scoreTable.length - 1)
console.log(average)

for (let i = 1; i < scoreTable.length; i++){
    if (parseInt(scoreTable[i].cells[1].textContent) > average){
        scoreTable[i].style.backgroundColor = "lightgreen"
    }
}

const newRow = document.createElement("tr");
const cell1 = document.createElement("td");
cell1.textContent = "Class Average:"

const cell2 = document.createElement("td");
cell2.textContent = average

newRow.appendChild(cell1);
newRow.appendChild(cell2);

table.appendChild(newRow);