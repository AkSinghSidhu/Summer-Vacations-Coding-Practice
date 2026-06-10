// HTML has only `<div id="app"></div>`. Build everything in JS: 5 cards each with a title, description, and Delete button. Delete removes only that card. An "Add Card" button creates a new one with placeholder content. A counter somewhere shows current card count and stays accurate.

const application = document.querySelector("#app")

const addBtn = document.createElement("button");
addBtn.textContent = "Add Card";
application.appendChild(addBtn);

let count = 0;
const counter = document.createElement("p");
application.appendChild(counter);

function cardContent(divCard, titleCard, descriptionCard){
    const title = document.createElement("h1");
    title.textContent = titleCard;
    divCard.appendChild(title);

    const para = document.createElement("p");
    para.textContent = descriptionCard;
    divCard.appendChild(para);
}

function createCard() {
    const divCard = document.createElement("div");
    divCard.className = "cards";

    cardContent(divCard,"Title", "Description Text")

    const btnDel = document.createElement("button");
    btnDel.textContent = "Delete";

    
  
    divCard.appendChild(btnDel);

    btnDel.addEventListener("click", () => {
        divCard.remove();
        count -= 1;
        counter.textContent = `Cards: ${count}`;
    });

    application.appendChild(divCard);
    count += 1;
    counter.textContent = `Cards: ${count}`;
}


for (let i = 0; i < 5; i++) {
    createCard();
}

addBtn.addEventListener("click", () => {
    createCard();
});

