#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    list_no_dup = [x for i, x in enumerate(my_list) if x not in my_list[:i]]
    for i in range(len(list_no_dup)):
        total += list_no_dup[i]

    return (total)
