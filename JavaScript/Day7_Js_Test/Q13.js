// Build an in-memory quiz engine. No classes, no DOM. Has: a list of 5 question objects `{question, options[], correctIndex}`, `checkAnswer(qIndex, answerIndex)` → true/false, `getScore()` → `"3/5 — 60%"`, `getWrongAnswers()` → array of questions missed. The score must not be directly modifiable from outside — only `checkAnswer` can change it.

function createQuiz(){
    let wrongAnsArr = [];
    let sum = 0;
    return{
        checkAnswer(qIndex, answerIndex){
            console.log(`Q${qIndex + 1}: ${Qlist[qIndex].question}`);
            console.log(`Your Answer: ${answerIndex}`);
            if (answerIndex === Qlist[qIndex].correctIndex){
                sum++;
                return true;
            }else{
                wrongAnsArr.push(Qlist[qIndex]);
                return false
            }
        },

        getScore(){
            let scoreStr = `${sum}/${length} — ${(sum / length) * 100}%`
            return scoreStr
        },

        getWrongAnswers(){
            return wrongAnsArr;
        }
    }
}

const Qlist = [
  {
    question: "What is the capital of France?",
    options: ["Berlin", "Madrid", "Paris", "Rome"],
    correctIndex: 2
  },
  {
    question: "Which language runs natively in web browsers?",
    options: ["Python", "Java", "JavaScript", "C++"],
    correctIndex: 2
  },
  {
    question: "What is 12 × 8?",
    options: ["96", "88", "108", "92"],
    correctIndex: 0
  },
  {
    question: "Which planet is known as the Red Planet?",
    options: ["Venus", "Mars", "Jupiter", "Mercury"],
    correctIndex: 1
  },
  {
    question: "Which data structure uses key-value pairs?",
    options: ["Array", "Tuple", "Dictionary", "Set"],
    correctIndex: 2
  }
];

const length =  Qlist.length
const quiz = createQuiz();

let ans1 = quiz.checkAnswer(0, 2);
console.log(ans1);
let ans2 = quiz.checkAnswer(1, 2);
console.log(ans2);
let ans3 = quiz.checkAnswer(2, 1);
console.log(ans3);
let ans4 = quiz.checkAnswer(3, 1);
console.log(ans4);
let ans5 = quiz.checkAnswer(4, 2);
console.log(ans5);

console.log("Total Score & Percentage:", quiz.getScore())
console.log("Questions that got answered wrong:", quiz.getWrongAnswers())