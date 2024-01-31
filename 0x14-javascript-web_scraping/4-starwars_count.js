#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided as a command-line argument
if (process.argv.length < 3) {
  console.error('Please provide the Star Wars API URL.');
  process.exit(1); // Exit with a non-zero status to indicate an error
}

const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API to get the list of films
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurred during the request, print the error message
    console.error(error);
  } else if (response.statusCode !== 200) {
    // If the request was not successful, print the status code
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
  } else {
    try {
      // Parse the JSON response
      const filmsData = JSON.parse(body);

      // Filter films where "Wedge Antilles" (character ID 18) is present
      const filmsWithWedge = filmsData.results.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));

      // Print the number of films with Wedge Antilles
      console.log(filmsWithWedge.length);
    } catch (parseError) {
      // If an error occurred during parsing, print the error message
      console.error(`Error parsing the response: ${parseError.message}`);
    }
  }
});
