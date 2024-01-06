#!/usr/bin/python3
"""This module provides a function that identifies the peak
_from a list of unsorted numbers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using binary search.

    Args:
        - list_of_integers: A list of unsorted integers.

    Returns:
        - The peak element
    """
    if not list_of_integers:
        return None     # Handle empty list

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            # Peak may be on the left half
            high = mid
        else:
            # Peak must be on the right half
            low = mid + 1

    # 'low' is the inde of the peak
    return list_of_integers[low]
