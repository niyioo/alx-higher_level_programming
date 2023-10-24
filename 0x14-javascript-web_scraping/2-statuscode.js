#!/usr/bin/node

const request = require('request');

const url = process.argv[2]; // Get the URL to request from the command line argument

if (!url) {
  console.error('Usage: node 2-status_code.js <URL>');
  process.exit(1);
}

// Make a GET request to the specified URL
request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
