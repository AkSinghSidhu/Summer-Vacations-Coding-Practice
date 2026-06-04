// Given `"  the quick brown fox  "`, produce `"The Quick Brown Fox"` — trimmed and title-cased — without retyping it. Log its final length, and whether it contains the word "fox" (case-insensitive check). Use your name variable from Day 1 somewhere in the final log line.

let str = "  the quick brown fox  ";
let str1 = str.trim();
const name = "Akash";

const indexOfthe = str1.indexOf("the"),
    indexOfquick = str1.indexOf("quick"),
    indexOfbrown = str1.indexOf("brown"),
    indexOffox = str1.indexOf("fox");

let str2 = str1[indexOfthe].toUpperCase() + str1.slice(indexOfthe + 1, indexOfquick) + str1[indexOfquick].toUpperCase() + str1.slice(indexOfquick + 1, indexOfbrown) + str1[indexOfbrown].toUpperCase() + str1.slice(indexOfbrown + 1, indexOffox) + str1[indexOffox].toUpperCase() + str1.slice(indexOffox + 1);

console.log(str2);
console.log(`The Length of the New String is: ${str2.length} and Does it includes the word "fox": ${str2.toLowerCase().includes("fox")}, also my name is: ${name}`);