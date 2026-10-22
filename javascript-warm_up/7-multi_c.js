#!/usr/bin/node
const occurrences = parseInt(process.argv[2], 10);

if (Number.isNaN(occurrences)) {
  console.log('Missing number of occurrences');
} else {
  let count = 0;

  while (count < occurrences) {
    console.log('C is fun');
    count += 1;
  }
}
