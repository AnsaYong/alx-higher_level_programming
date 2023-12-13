#!/usr/bin/node

exports.converter = function (base) {
  const digits = '0123456789abcdef';

  function convertToBase (number) {
    if (number < base) {
      return digits.charAt(number);
    }
    return convertToBase(Math.floor(number / base)) + digits.charAt(number % base);
  }

  return convertToBase;
};
