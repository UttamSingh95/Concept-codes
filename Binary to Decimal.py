"""
Problem Description

You are given a number A in binary format (Base = 2). You have to print the number in decimal format (Base = 10).
"""

"""
explaination link: https://www.rapidtables.com/convert/number/binary-to-decimal.html
"""


def decimal_converter():
    num = input()

    ans = 0
    place = len(num)
    for x in num:
        ans = ans + (int(x) * (2 ** (place - 1)))
        place -= 1
    print(ans)

decimal_converter()
