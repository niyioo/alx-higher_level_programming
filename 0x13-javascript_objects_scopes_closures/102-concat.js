#!/usr/bin/node

// Import the 'fs' (File System) module
const fs = require('fs');

// Read the content of the first source file (specified by the first command-line argument)
const src1 = fs.readFileSync(process.argv[2], 'utf8');

// Read the content of the second source file (specified by the second command-line argument)
const src2 = fs.readFileSync(process.argv[3], 'utf8');

// Concatenate the contents of the two source files
const concatenatedContent = src1 + src2;

// Write the concatenated content to the destination file (specified by the third command-line argument)
fs.writeFileSync(process.argv[4], concatenatedContent);

// Print a message indicating that the files were concatenated successfully
console.log(`Concatenated ${process.argv[2]} and ${process.argv[3]} to ${process.argv[4]}`);
