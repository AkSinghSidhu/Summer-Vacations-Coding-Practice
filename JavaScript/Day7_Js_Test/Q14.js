//  Build a data pipeline. Write `pipe(...fns)` and use it to clean raw user strings like `"  john doe , 25 , new york  "`. The pipeline: trims, splits by comma, strips each part, builds `{name, age, city}`, filters out anyone under 18. Input is an array of 6 such strings. Return the final clean array.

function pipe(...fns){
    return function(input) {
        return fns.reduce((acc, fn) => fn(acc), input)
    }
}

function trim(str) {
    return str.trim();
}

function split(str){
    return str.split(",");
}

function strip(str){
    return str.map(element => element.trim());
}

function build(str){
    let dict = {name: str[0], age : parseInt(str[1]), city: str[2]};
    return dict
}


let listOfStr = [
    "  john doe  , 16 ,  new york  ",
    "emma stone ,30, los angeles   ",
    " liam smith,  22 ,chicago",
    "olivia brown   , 28 ,  london  ",
    "noah johnson,35 , toronto   ",
    " sophia davis , 27,  sydney  "
];

const pipeline = pipe(trim, split, strip, build);
const result = listOfStr.map(strings => pipeline(strings)).filter(person => person.age >= 18);
console.log(result);

