#!/usr/bin/node

// Initialize a count to keep track of the number of arguments already printed
let count = 0;

// Function to print the number of arguments already printed and the new argument value
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
