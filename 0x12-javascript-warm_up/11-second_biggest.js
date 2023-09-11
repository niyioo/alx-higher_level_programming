#!/usr/bin/node
function findSecondLargest(arr) {
    if (arr.length < 2) {
        return 0;
    }
    let firstMax = -Infinity;
    let secondMax = -Infinity;
    for (let num of arr) {
        num = parseInt(num);
        if (num > firstMax) {
            secondMax = firstMax;
            firstMax = num;
        } else if (num > secondMax && num < firstMax) {
            secondMax = num;
        }
    }
    return secondMax;
}
const args = process.argv.slice(2);
const secondLargest = findSecondLargest(args);
console.log(secondLargest);