#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const l in list) {
    if (list[l] === searchElement) {
      count++;
    }
  }
  return count;
};
