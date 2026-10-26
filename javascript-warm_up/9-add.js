#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const first = parseInt(process.argv[2], 10);
const second = parseInt(process.argv[3], 10);

add(first, second);
