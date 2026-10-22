#!/usr/bin/node
const request = require('request');

request.get(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    if (response.statusCode < 200 || response.statusCode >= 300) {
      console.error(`Request failed with status code ${response.statusCode}`);
      return;
    }

    let film;
    try {
      film = JSON.parse(body);
    } catch (parseError) {
      console.error(parseError);
      return;
    }

    Promise.all(film.characters.map((url) => new Promise((resolve, reject) => {
      request.get(url, (characterError, characterResponse, characterBody) => {
        if (characterError) {
          reject(characterError);
          return;
        }

        if (characterResponse.statusCode < 200 ||
          characterResponse.statusCode >= 300) {
          reject(new Error(
            `Request failed with status code ${characterResponse.statusCode}`
          ));
          return;
        }

        try {
          resolve(JSON.parse(characterBody).name);
        } catch (parseError) {
          reject(parseError);
        }
      });
    }))).then((names) => {
      names.forEach((name) => console.log(name));
    }).catch((characterError) => {
      console.error(characterError);
    });
  }
);
