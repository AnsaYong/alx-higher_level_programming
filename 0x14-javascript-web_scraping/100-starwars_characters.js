#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (error, _, body) => {
  if (error) {
    console.error(error);
  } else {
    JSON.parse(body).characters.forEach((character) => {
      request(character, (error, _, body) => {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
