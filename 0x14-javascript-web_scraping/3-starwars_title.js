#!/usr/bin/node

const request = require('request');

const episodeNumber = process.argv[2]; // Get the movie ID (episode number) from the command line argument

if (!episodeNumber) {
  console.error('Usage: node 3-starwars_title.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${episodeNumber}`;

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } else {
    console.error(`Request failed with status code: ${response.statusCode}`);
  }
});
