#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: node concat-files.js <sourceFile1> <sourceFile2> <destinationFile>');
  process.exit(1); // Exit with an error code
}

// Get the source file paths and destination file path from command-line arguments
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Read the content of the first source file
fs.readFile(sourceFile1, 'utf8', (err1, data1) => {
  if (err1) {
    console.error(`Error reading ${sourceFile1}: ${err1.message}`);
    process.exit(1); // Exit with an error code
  }

  // Read the content of the second source file
  fs.readFile(sourceFile2, 'utf8', (err2, data2) => {
    if (err2) {
      console.error(`Error reading ${sourceFile2}: ${err2.message}`);
      process.exit(1); // Exit with an error code
    }

    // Concatenate the content of the two source files
    const concatenatedData = data1 + data2;

    // Write the concatenated data to the destination file
    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err3) => {
      if (err3) {
        console.error(`Error writing to ${destinationFile}: ${err3.message}`);
        process.exit(1); // Exit with an error code
      }

      console.log(`Concatenated ${sourceFile1} and ${sourceFile2} to ${destinationFile}`);
    });
  });
});
