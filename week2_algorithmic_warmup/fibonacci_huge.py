# Uses python3
import sys


def calc_fib(n):
    """Fibonacci sequence"""
    # if n <= 1:
    #     return n
    #
    # return calc_fib(n - 1) + calc_fib(n - 2)
    seq = [0, 1]
    for i in range(2, n+1):
        seq.append(seq[i-2] + seq[i-1])
    return seq[n]


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    period = get_pisano_period(m)
    return (calc_fib(n % period)) % m


def get_pisano_period(m) -> int:
    found = False
    i = 0
    prev = 0
    curr = 1
    while not found:
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            return i + 1
        i += 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
    # numbers = input("Enter numbers: ")
    # n, m = int(numbers.split()[0]), int(numbers.split()[1])
    # print(get_fibonacci_huge_naive(n, m))
