#!/usr/bin/node

const myVar = process.argv;
const size = Number(myVar[2]);

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'x';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
