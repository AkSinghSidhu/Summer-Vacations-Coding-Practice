// Log the result and type of each: `"5" + 3`, `"5" - 3`, `true + 1`, `null + 1`, `undefined + 1`. Write a comment next to each explaining what JS did. This will require looking things up — that's the point.

console.log("5" + 3); // Since "5" is a string and we are using "+" which essentially concatenates the "5" and 3, while treating 3 as string rather than number.
console.log("5" - 3); // Since "5" is a string and we are using "-" which treats the "5" as number (converts the string to number), and then performs the difference operations simply.
console.log(true + 1); // Since true means 1, we are simply adding 1 + 1 here
console.log(null + 1); // null is nothing or empty value, so simply 0 + 1
console.log(undefined + 1); // Undefined means not defined, since no value is defined we cannot operate on Undefined value, so it gives NaN which represents computational error