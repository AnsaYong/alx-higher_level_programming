#!/usr/bin/node

const myVar = process.argv;

if (!isNaN(Number(myVar[2]))) {
  console.log(`My number: ${Number(myVar[2])}`);
} else {
  console.log('Not a number');
}
