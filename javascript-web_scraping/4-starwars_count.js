#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode < 200 || response.statusCode >= 300) {
    console.error(`Request failed with status code ${response.statusCode}`);
    return;
  }

  let data;
  try {
    data = JSON.parse(body);
  } catch (parseError) {
    console.error(parseError);
    return;
  }

  const count = data.results.filter((film) => film.characters.some((url) => {
    return new URL(url).pathname.replace(/\/$/, '').split('/').pop() === '18';
  })).length;

  console.log(count);
});
