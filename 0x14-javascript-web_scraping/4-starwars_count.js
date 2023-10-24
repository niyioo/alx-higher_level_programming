#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from the command line argument

if (!apiUrl) {
  console.error('Usage: node 4-starwars_count.js <api_url>');
  process.exit(1);
}

const characterId = 18; // Character ID for Wedge Antilles

// Make a GET request to the Star Wars API to fetch the list of films
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const wedgeAntillesFilms = filmData.results.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    console.log(wedgeAntillesFilms.length);
  } else {
    console.error(`Request failed with status code: ${response.statusCode}`);
  }
});
