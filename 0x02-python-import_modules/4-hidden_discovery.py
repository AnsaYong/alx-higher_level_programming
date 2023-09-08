#!/usr/bin/python3
if __name__ == "__main__":
    import sys, hidden_4

    for i in range(len(dir(hidden_4))):
        if dir(hidden_4)[i][0] != "_":
            print("{}".format(dir(hidden_4)[i]))
