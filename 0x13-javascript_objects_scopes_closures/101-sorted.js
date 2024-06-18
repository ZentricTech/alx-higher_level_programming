#!/usr/bin/node
const dict = require('./101-data').dict;
const dKeys = Object.keys(dict);
const convertedArr = Object.entries(dict);
const values = Object.values(dict);
let matched;
const newObj = {};
const result = {};
// loop over the values
for (let i = 0; i < values.length; i++) {
  result[JSON.stringify(values[i])] = [];
  matched = dKeys.filter(key => dict[key] === values[i]);
  matched.forEach(item => result[JSON.stringify(values[i])].push(item));
}
console.log(result)
convertedArr.forEach(element => {
  newObj[element[1]] ? newObj[element[1]].push(element[0]) : newObj[element[1]] = [element[0]];
});

console.log(newObj);
