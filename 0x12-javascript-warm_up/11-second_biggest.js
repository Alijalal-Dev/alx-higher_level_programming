#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const secondBiggestNumber = process.argv.map(Number)
    .filter(Number)
    .sort((a, b) => b - a)[1];
  console.log(secondBiggestNumber);
}
