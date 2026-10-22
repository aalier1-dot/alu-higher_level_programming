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

    const printCharacter = (index) => {
      if (index >= film.characters.length) {
        return;
      }

      request.get(film.characters[index], (characterError, characterResponse,
        characterBody) => {
        if (characterError) {
          console.error(characterError);
          return;
        }

        if (characterResponse.statusCode < 200 ||
          characterResponse.statusCode >= 300) {
          console.error(
            `Request failed with status code ${characterResponse.statusCode}`
          );
          return;
        }

        let character;
        try {
          character = JSON.parse(characterBody);
        } catch (parseError) {
          console.error(parseError);
          return;
        }

        console.log(character.name);
        printCharacter(index + 1);
      });
    };

    printCharacter(0);
  }
);
