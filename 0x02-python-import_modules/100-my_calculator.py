#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    n = 0
    operators = ["+", "-", "*", "/"]

    # check if there are 3 arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    # Check if the provided operator is valid
    for i in range(len(operators)):
        if operators[i] == sys.argv[2]:
            n = 1
    if n != 1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    # Execute the operation
    if sys.argv[2] == "+":
        result = calculator_1.add(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "-":
        result = calculator_1.sub(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "*":
        result = calculator_1.mul(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "/":
        result = calculator_1.div(int(sys.argv[1]), int(sys.argv[3]))

    # Print result to standard output
    print("{} {} {} = {}".format(sys.argv[1],
          sys.argv[2], sys.argv[3], result))
