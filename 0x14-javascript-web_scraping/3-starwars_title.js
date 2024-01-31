#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Please provide the movie ID.');
  process.exit(1);
}

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    // If the request was not successful, print the status code
    console.error(response.statusCode);
  } else {
    try {
      // Parse he JSON response
      const movieData = JSON.parse(body);

      // Print the tite of the movie
      console.log(movieData.title);
    } catch (parseError) {
      // If an error occurred during parsing, print the error message
      console.error(parseError.message);
    }
  }
});
