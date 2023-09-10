#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()   # deep copy - both lists not linked
    if idx < 0 or idx > (len(my_list) - 1):
        return (new_list)
    else:
        new_list[idx] = element
        return (new_list)
