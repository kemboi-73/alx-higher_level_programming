#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => b - a); // Sort the numbers in descending order
  const secondLargest = args[1]; // Get the second element (the second largest)
  console.log(secondLargest);
}

