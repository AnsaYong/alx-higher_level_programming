#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (error, _, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = [];

    JSON.parse(body).characters.forEach((character) => {
      characters.push(new Promise((resolve, reject) =>
        request(character, function (error, _, body) {
          if (error) {
            reject(error);
          }
          resolve(JSON.parse(body).name);
        })));
    });

    Promise.all(characters)
      .then((names) => {
        names.forEach((name) => {
          console.log(name);
        });
      });
  }
});
