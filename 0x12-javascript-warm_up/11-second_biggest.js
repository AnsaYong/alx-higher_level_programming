#!/usr/bin/node

function secondLargest (args) {
  args.sort((a, b) => b - a); // Sort in descending order - handles numbers correctly and not as strings
  return args[1]; // Index 1 corresponds to the second largest element
}

const myVar = process.argv.slice(2); // Exclude the first two elements

if (myVar.length < 2) {
  console.log(0);
} else {
  console.log(`${secondLargest(myVar)}`);
}
