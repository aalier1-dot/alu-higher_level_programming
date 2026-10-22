#!/usr/bin/node
const fs = require('fs');
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

  fs.writeFile(process.argv[3], body, 'utf8', (writeError) => {
    if (writeError) {
      console.error(writeError);
    }
  });
});
