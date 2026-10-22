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

    console.log(film.title);
  }
);
