// Take any sentence string. Write code that: splits into words, reverses the word order, capitalizes the last letter of each word, and joins back into one string. Log the original and the result. Also log how many words in the original were longer than 4 characters.

let str = "I am a Btech Student";

let arr = str.split(" ").reverse();

let upperCased = arr.map(element => {
    let x = element.length - 1;
    return element.slice(0,-1) + element.charAt(x).toUpperCase();
    
})

let str1 = upperCased.join(" ");
console.log(`Original: ${str} \nResult: ${str1}`);

console.log(`Words longer than 4 characters: ${arr.filter(element => element.length > 4).length}`)