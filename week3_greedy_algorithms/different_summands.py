# Uses python3
import sys


def optimal_summands(n):
    summands = []
    sum_ = 0
    i = 1
    while sum_ != n:
        if (sum_ + i) + (i + 1) <= n:
            sum_ += i
            summands.append(i)
            i += 1
        else:
            add_num = n - sum_
            sum_ = n
            summands.append(add_num)
    return summands


if __name__ == '__main__':
    # input = input("number: ")
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
