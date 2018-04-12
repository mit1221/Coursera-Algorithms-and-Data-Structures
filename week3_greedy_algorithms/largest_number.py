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


def isGreaterOrEqual(num1, num2) -> bool:
    """Return True if num1 is greater than or equal to num2"""
    num1_list = [num1[i] for i in range(len(num1))]
    num2_list = [num2[i] for i in range(len(num2))]
    i = 0
    j = 0
    counter = 0
    while counter != max(len(num1_list), len(num2_list)):
        if num1_list[i] > num2_list[j]:
            return True
        elif num1_list[i] < num2_list[j]:
            return False
        else:
            if i + 1 <= len(num1_list) - 1:
                i += 1
            if j + 1 <= len(num2_list) - 1:
                j += 1
        counter += 1
    return True


if __name__ == '__main__':
    # input = input("enter: ")
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
