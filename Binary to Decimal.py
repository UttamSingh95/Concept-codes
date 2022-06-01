"""
Problem Description

You are given a number A in binary format (Base = 2). You have to print the number in decimal format (Base = 10).
"""

"""
explaination link: https://www.rapidtables.com/convert/number/binary-to-decimal.html
"""

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    def decimal_converter():
        num = input()

        ans = 0
        place = len(num)
        for x in num:
            ans = ans + (int(x) * (2 ** (place - 1)))
            place -= 1
        print(ans)

    decimal_converter()


    return 0

if __name__ == '__main__':
    main()