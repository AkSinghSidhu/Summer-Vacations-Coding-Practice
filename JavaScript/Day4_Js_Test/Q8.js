// Create an array of 5 student objects: `{name, grade, passed}`. Using array methods: get names of all who passed, calculate class average, find the top scorer, build a new array of strings like `"Akash: 88 ✓"` or `"Ravi: 45 ✗"` for every student.

let students = [
    {
        name : "Random1",
        score : 93,
        passed : true
    },
    {
        name : "Random2",
        score : 45,
        passed : false
    },
    {
        name : "Random3",
        score : 53,
        passed : true
    },
    {
        name : "Random4",
        score : 82,
        passed : true
    },
    {
        name : "Random5",
        score : 67,
        passed : true
    }
]
let lenOfArray = students.length;
let passedStudent = students.filter(student => student.passed);
console.log("Students who Passed: ", passedStudent.map(names => names.name))
let sumOfElements = students.reduce((sum, num) => sum + num.score , 0);
let average = sumOfElements / lenOfArray;
console.log(`Class Average: ${average}`);

console.log("Top Scorer: ", students.reduce((max, num) => num.score > max.score ? num : max).name);

let newArray = students.map(student => student.passed ? `${student.name}: ${student.score} ✓` : `${student.name}: ${student.score} ✗`);
console.log(newArray)