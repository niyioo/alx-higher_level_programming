#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // Get the URL to request from the command line argument
const filePath = process.argv[3]; // Get the file path to store the response from the command line argument

if (!url || !filePath) {
  console.error('Usage: node 5-request_store.js <URL> <file_path>');
  process.exit(1);
}

// Make a GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Write the body response to the specified file (UTF-8 encoded)
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      } else {
        console.log(`Content from ${url} has been saved to ${filePath}`);
      }
    });
  }
});
