#!/usr/bin/python3
def no_c(my_string):
    # Using list comprehension
    return ''.join([char for char in my_string if char not in 'cC'])
