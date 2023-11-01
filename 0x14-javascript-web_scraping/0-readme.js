#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from the command line argument

if (!filePath) {
  console.error('Usage: node 0-readme.js <file_path>');
  process.exit(1);
}

// Read the content of the file
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
