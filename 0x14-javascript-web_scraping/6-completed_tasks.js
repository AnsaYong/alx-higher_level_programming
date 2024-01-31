#!/usr/bin/node
// Script that computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, (error, _, body) => {
  if (error) {
    console.error(error);
  } else {
    const result = {};

    JSON.parse(body).forEach((data) => {
      if (data.completed) {
        if (!(data.userId in result)) {
          result[data.userId] = 0;
        }
        result[data.userId] += 1;
      }
    });

    console.log(result);
  }
});
