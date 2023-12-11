#!/usr/bin/node

const myVar = process.argv.length;

if (myVar > 3) {
  console.log('Arguments found');
} else if (myVar === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
