// Store 5 subject names and scores. Calculate the average. Use a ternary to assign a letter grade (A: 90+, B: 80+, C: 70+, F: below). Log: `"Student: Akash | Average: 85.4 | Grade: B"` — all computed, nothing hardcoded.

let student_name = "Akash";
const math = 80,
    physics = 78,
    chemistry = 82,
    english = 95,
    agriculture = 93;

let average = (math + physics + chemistry + english + agriculture) / 5;

let grade = average > 90 ? "A":
    average > 80 ? "B":
    average > 70 ? "C":
    "F";

console.log(`Student: ${student_name} | Average: ${average} | Grade: ${grade}`);