#!/usr/bin/node

const myVar = process.argv;

function add (a, b) {
  const result = a + b;
  return result;
}

const sum = add(Number(myVar[2]), Number(myVar[3]));
console.log(sum);
