#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if both URL and file path are provided as command-line arguments
if (process.argv.length < 4) {
  console.error('Please provide both the URL to request and the file path to store the response.');
  process.exit(1); // Exit with a non-zero status to indicate an error
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request using request
request.get({ url, encoding: 'utf-8' }, (error, response, body) => {
  if (error) {
    // If an error occurred during the request, print the error message
    console.error(error.message);
  } else if (response.statusCode !== 200) {
    // If the request was not successful, print the status code
    console.error(response.statusMessage);
  } else {
    // Write the body response to the specified file
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        // If an error occurred during writing, print the error message
        console.error(writeError.message);
      }
    });
  }
});
