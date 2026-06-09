// HTML file with: a `<h1>`, an empty `<div id="info">`, a `<p>` with some text, and a `<ul>` with 4 items. Using JS only after page loads: change the heading to your name, put today's date in the div, replace the paragraph text with the item count, change body background color using a variable. No CSS file.

const title = document.querySelector("h1");
title.textContent = "Akash"

const div = document.querySelector("#info");
const today = new Date();
div.innerHTML = (`${today.getUTCDate()}/${today.getMonth() + 1}/${today.getFullYear()}`);

const uList = document.querySelectorAll("ul li");
const para = document.querySelector("p");
para.innerHTML = uList.length;

const bodyColor = document.querySelector("body");
bodyColor.style.color = "White";
bodyColor.style.backgroundColor = "blue";