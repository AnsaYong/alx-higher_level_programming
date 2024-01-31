#!/usr/bin/node

const fileSystem = require('fs');

// Check if the file path is provided as a comman-line argument
if (process.argv.length < 3) {
  console.error('Please provide the file path.');
  process.exit(1); // Exit with a non-zero status to indicate error
}

const filePath = process.argv[2];

// Read the content of the file in utf-8
fileSystem.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // If an error occurred during reading, print the error object
    console.error(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
