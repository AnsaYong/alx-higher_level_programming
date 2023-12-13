#!/usr/bin/node

exports.esrever = function (list) {
  let i = 0;
  let j = list.length - 1;
  const newList = [];
  while (i < list.length) {
    newList[j] = list[i];
    i++;
    j--;
  }
  return newList;
};
