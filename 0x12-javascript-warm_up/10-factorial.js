#!/usr/bin/node

function factorial(n) {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  }
  if (n === 0) {
    return 1; // Factorial of 0 is 1
  }
  if (n < 0) {
    return Infinity; // Factorial of a negative number is Infinity
  }
  return n * factorial(n - 1);
}

const args = process.argv.slice(2);
const n = parseInt(args[0]);

console.log(factorial(n));

