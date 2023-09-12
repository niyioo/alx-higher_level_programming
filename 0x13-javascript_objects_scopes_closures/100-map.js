#!/usr/bin/node

// Import the list from 100-data.js
const { list } = require('./100-data');

// Use the map function to create a new array
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log('Initial List:', list);
console.log('New List:', newList);
