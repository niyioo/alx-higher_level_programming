#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from the command line argument

if (!movieId) {
  console.error('Usage: node 101-starwars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API to fetch movie data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Retrieve character data for each character URL in order
    const characterPromises = characterUrls.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (characterError, characterResponse, characterBody) => {
          if (!characterError && characterResponse.statusCode === 200) {
            const characterData = JSON.parse(characterBody);
            resolve(characterData.name);
          } else {
            reject(characterError);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then((characters) => {
        characters.forEach((character) => {
          console.log(character);
        });
      })
      .catch((error) => {
        console.error(error);
      });
  } else {
    console.error(`Request failed with status code: ${response.statusCode}`);
  }
});
