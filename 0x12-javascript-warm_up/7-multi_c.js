#!/usr/bin/node

const myVar = process.argv;
const x = Number(myVar[2]);
let i = 0;

if (!isNaN(x)) {
  for (;i < x;) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
