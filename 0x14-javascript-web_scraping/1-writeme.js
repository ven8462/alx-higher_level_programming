#!/usr/bin/node

const fs = require('fs');

// Get the file path from the first argument
const filePath = process.argv[2];

// Get the string to write from the second argument
const stringToWrite = process.argv[3];

// Write the string to the file
fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    // If an error occurred, print the error object
    console.error(err);
  } else {
    // If no error occurred, print a success message
    console.log(stringToWrite);
  }
});
