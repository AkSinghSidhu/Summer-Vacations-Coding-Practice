// Declare two numbers. Calculate and log: their sum, difference, product, remainder when first is divided by second, and first to the power of second. Then log two more things: is the sum greater than 50? Is the product even? Figure out what operator checks remainder and what checks power.

let num1 = 10, num2 = 20;

sum = num1 + num2;
difference = num1 - num2;
product = num1 * num2;
remainder = num1 % num2;
power = num1 ** num2;

console.log(`Sum: ${sum}, Difference: ${difference}, Product: ${product}, Remainder: ${remainder}, Power: ${power}`);

let isGreater = sum > 50;
let isEven = product % 2 == 0;

console.log(`Is the sum greater than 50?: ${isGreater} & Is the product even?: ${isEven}`);