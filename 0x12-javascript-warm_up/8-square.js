#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!isNaN(size)) {
  if (size > 0) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
    console.log('');
  }
} else {
    console.log('Missing size');
}
