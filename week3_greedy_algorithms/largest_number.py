#Uses python3

import sys


def largest_number(a):
    answer = ''
    while a != []:
        max_digit = None
        for digit in a:
            if max_digit is None or isGreaterOrEqual(digit, max_digit):
                max_digit = digit
        answer += max_digit
        a.remove(max_digit)
    return answer


def isGreaterOrEqual(a, b) -> bool:
    str1 = str(a) + str(b)
    str2 = str(b) + str(a)
    if int(str1) < int(str2):
        return False
    else:
        return True


if __name__ == '__main__':
    # input = input("enter: ")
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
