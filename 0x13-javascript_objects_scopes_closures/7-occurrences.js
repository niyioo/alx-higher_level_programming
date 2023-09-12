#!/usr/bin/node

// Function to count the number of occurrences of a specific element in a list
exports.nbOccurences = (list, searchElement) => {
  // Initialize a count variable to keep track of occurrences
  let count = 0;

  // Iterate through the list using a forEach loop
  list.forEach((element) => {
    if (element === searchElement) {
      count++;
    }
  });

  // Return the final count
  return count;
};
