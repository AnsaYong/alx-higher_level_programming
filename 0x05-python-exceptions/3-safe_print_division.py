#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        return (None)
    finally:
        try:
            print("Inside result: {}".format(div))
        except UnboundLocalError:
            print("Inside result: {}".format(None))

    return (div)
