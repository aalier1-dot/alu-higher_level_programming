#!/usr/bin/node
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .done((data) => {
    $('#character').text(data.name);
  })
  .fail((error) => {
    console.error(error);
  });
