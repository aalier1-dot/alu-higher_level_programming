#!/usr/bin/node
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json')
  .done((data) => {
    data.results.forEach((film) => {
      $('#list_movies').append($('<li>').text(film.title));
    });
  })
  .fail((error) => {
    console.error(error);
  });
