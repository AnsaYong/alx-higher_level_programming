#!/usr/bin/node

const fs = require('fs');

// Check if both file path and string towrite are provided
if (process.argv.length < 4) {
  console.error('Please provide both the file path and the string too write');
  process.exit(1);
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write the content to the file in utf-8
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
