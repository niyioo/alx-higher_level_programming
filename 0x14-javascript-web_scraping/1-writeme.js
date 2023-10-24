#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from the first command line argument
const content = process.argv[3]; // Get the string to write from the second command line argument

if (!filePath || !content) {
  console.error('Usage: node 1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

// Write the content to the file
fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
