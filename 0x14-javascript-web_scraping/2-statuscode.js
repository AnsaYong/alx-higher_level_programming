#!/usr/bin/node

const request = require('request');

// Check if the URL is provided as a command-line argument
if (process.argv.length < 3) {
  console.error('Please provide the URL to request.');
  process.exit(1);
}

const url = process.argv[2];

// Make a GET request using request
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    // Print the status code if no error
    console.log(`code: ${response.statusCode}`);
  }
});
