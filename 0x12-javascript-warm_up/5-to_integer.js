#!/usr/bin/node

const firstArgv = process.argv[2];
const num = parseInt(firstArgv);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ', num);
}
