// You have an array of 6 objects: `{title, color}`. Build a grid of colored boxes with titles entirely in JS. Clicking a box toggles a "selected" class on it. Show how many boxes are currently selected. A "Clear" button deselects all. No hardcoded HTML boxes.

const boxes = [
    { title: "Box 1", color: "red" },
    { title: "Box 2", color: "blue" },
    { title: "Box 3", color: "pink" },
    { title: "Box 4", color: "lightblue" },
    { title: "Box 5", color: "purple" },
    { title: "Box 6", color: "white" },
]

const body = document.querySelector("body");

const container = document.createElement("div");
container.id = "container";
body.appendChild(container)

let count = 0;
const counter = document.createElement("p");
container.appendChild(counter);

const btn = document.createElement("button");
btn.textContent = "Clear";
container.appendChild(btn);

for (let i = 0; i < boxes.length; i++){
    const divBox = document.createElement("div");
    container.appendChild(divBox);
    divBox.style.width = "100px";
    divBox.style.height = "100px";

    const para = document.createElement("p");
    para.innerHTML = `<b>${boxes[i].title}</b>`;
    divBox.appendChild(para);
    divBox.style.color = "white"
    divBox.style.webkitTextStroke = "0.5px black"
    divBox.style.backgroundColor = boxes[i].color



    counter.textContent = `Selected: ${count}`;
    divBox.addEventListener("click", () => {
        divBox.classList.toggle("selected");
        if (divBox.classList.contains("selected")) {
            count++;
        } else {
            count--;
        }
        counter.textContent = `Selected: ${count}`;
    })

    btn.addEventListener("click", () => {
    document.querySelectorAll(".selected").forEach(box => {
        box.classList.remove("selected");
    });
    count = 0;
    counter.textContent = `Selected: ${count}`;
});
}

