#!/usr/bin/node

const args = process.argv.slice(2);

function add (a, b) {
  if (isNaN(args[0]) || isNaN(args[1])) {
    console.log('NaN');
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}

add(args[0], args[1]);
