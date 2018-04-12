# Uses python3
import sys


def get_change(m):
    change = 0
    for i in (10, 5):
        change += m // i
        m %= i
    change += m
    return change


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
