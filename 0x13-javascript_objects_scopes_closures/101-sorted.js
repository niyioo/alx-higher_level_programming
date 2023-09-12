#!/usr/bin/node

// Import the dict from 101-data.js
const { dict } = require('./101-data');

// Initialize a new dictionary for user ids by occurrence
const userIdsByOccurrence = {};

// Iterate through the original dictionary
for (const userId in dict) {
  const occurrence = dict[userId];

  // Check if the occurrence count is already a key in the new dictionary
  if (userIdsByOccurrence[occurrence] === undefined) {
    // If not, initialize it with an empty array
    userIdsByOccurrence[occurrence] = [];
  }

  // Add the user id to the corresponding occurrence key
  userIdsByOccurrence[occurrence].push(parseInt(userId));
}

// Print the new dictionary
console.log(userIdsByOccurrence);
