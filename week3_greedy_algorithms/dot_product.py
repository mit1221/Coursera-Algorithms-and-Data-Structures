#Uses python3

import sys


def max_dot_product(a, b):
    max_product = 0
    for i in range(len(a)):
        max_a = max(a)
        a.remove(max_a)
        max_b = max(b)
        b.remove(max_b)
        max_product += max_a * max_b
    return max_product


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    # c = input("enter info: ")
    # d = c.split()
    # d = [int(i) for i in d]
    # n = d[0]
    # a = d[1:(n + 1)]
    # b = d[(n + 1):]
    # print(max_dot_product(a, b))
