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

  let todos;
  try {
    todos = JSON.parse(body);
  } catch (parseError) {
    console.error(parseError);
    return;
  }

  const completedTasks = {};
  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedTasks[todo.userId] === undefined) {
        completedTasks[todo.userId] = 0;
      }
      completedTasks[todo.userId] += 1;
    }
  });

  console.log(completedTasks);
});
