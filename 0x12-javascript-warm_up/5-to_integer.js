#!/usr/bin/nodejs

const arg1 = process.argv[2];

const parsedArg = parseInt(arg1);

if (!isNaN(parsedArg)) {
  console.log("My number: " + parsedArg);
} else {
  console.log("Not a number");
}

