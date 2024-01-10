#!/usr/bin/node
/*
searches the second biggest integer in the list of arguments.
*/
if (process.argv.length < 4) {
  console.log(0);
} else {
  const list = process.argv.slice(2).sort(function (a, b) { return b - a; });
  console.log(list[1]);
}
