// Declare 3 variables: your name (should never change after being set), your age (can change), and a score starting at 0. Reassign age and score. Try reassigning name and see what happens. Log all three in a single line as: `"Akash | Age: 22 | Score: 0"`.

const name = "Akash";
let age = 22, score = 0;

console.log(`${name} | Age: ${age} | Score: ${score}`);

age = 23;
score = 10;

console.log(`${name} | Age: ${age} | Score: ${score}`);

//Changing name would give "TypeError: Assignment to constant variable."