#!/usr/bin/node
function factorial(n) {
    if (isNaN(n)) {
        return 1; // Factorial of NaN is 1
    }
    if (n === 0 || n === 1) {
        return 1; // Factorial of 0 and 1 is 1
    } else {
        return n * factorial(n - 1); // Recursive calculation of factorial
    }
}
const arg = parseInt(process.argv[2]);
const result = factorial(arg);
console.log(result);