#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided as a command-line argument
if (process.argv.length < 3) {
  console.error('Please provide the API URL.');
  process.exit(1); // Exit with a non-zero status to indicate an error
}

const apiUrl = process.argv[2];

// Make a GET request to the API to get the list of tasks
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurred during the request, print the error message
    console.error(error.message);
  } else if (response.statusCode !== 200) {
    // If the request was not successful, print the status code
    console.error(response.statusMessage);
  } else {
    try {
      // Parse the JSON response
      const tasksData = JSON.parse(body);

      // Compute the number of completed tasks for each user
      const completedTasksByUser = {};
      tasksData.forEach(task => {
        if (task.completed) {
          if (completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId]++;
          } else {
            completedTasksByUser[task.userId] = 1;
          }
        }
      });

      // Print users with completed tasks
      console.log(JSON.stringify(completedTasksByUser, null, 2));
    } catch (parseError) {
      // If an error occurred during parsing, print the error message
      console.error(`Error parsing the response: ${parseError.message}`);
    }
  }
});
