#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            new_elt = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            new_elt = 0
        except TypeError:
            print("wrong type")
            new_elt = 0
        except IndexError:
            print("out of range")
            new_elt = 0
        finally:
            new_list.append(new_elt)

    return (new_list)
