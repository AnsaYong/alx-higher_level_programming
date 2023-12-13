#!/usr/bin/node

exports.converter = function (base) {
  function convertToBase (number) {
    if (number < base) {
      return '0123456789abcdef'.charAt(number);
    }
    return convertToBase(Math.floor(number / base)) + '0123456789abcdef'.charAt(number % base);
  }

  return convertToBase;
};
