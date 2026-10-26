#!/usr/bin/node

const number = process.argv[2];
const iteration = parseInt(number, 10);

if (isNaN(iteration)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < iteration; i++) {
    console.log('C is fun');
  }
}
