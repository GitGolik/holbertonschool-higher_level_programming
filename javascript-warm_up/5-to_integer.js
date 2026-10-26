#!/usr/bin/node

const myVar = process.argv[2];
const number = parseInt(myVar, 10);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number:', myVar);
}
