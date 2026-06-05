// Given `[3, 7, 2, 14, 8, 1, 22, 5, 18, 11]`, using only array methods (no for/while loops): filter numbers above 5, double each, sum them all, find the first number in the original array greater than 15, check if all numbers in the filtered+doubled array are above 10. Five operations, no loops.

let array = [3, 7, 2, 14, 8, 1, 22, 5, 18, 11];

let above5 = array.filter(num => num > 5);
console.log(above5)

above5 = above5.map(num => num * 2);
console.log(above5)

const sumOfArr = above5.reduce((sum, num) => sum + num);
console.log(sumOfArr)

console.log(array.find(num => num > 15));

console.log(above5.every(num => num >10));