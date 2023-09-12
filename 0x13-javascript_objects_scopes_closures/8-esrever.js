#!/usr/bin/node

// Function to reverse a list without using the built-in reverse method
exports.esrever = function (list) {
  // Check if the list is empty or has only one element (already reversed)
  if (list.length <= 1) {
    return list.slice(); // Return a copy of the original list
  }

  // Initialize an empty result array
  const reversedList = [];

  // Iterate through the original list in reverse order and append elements to the result array
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};
