# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    ratios = []
    for i in range(len(weights)):
        ratios.append(values[i] / weights[i])
    # ratios.sort(reverse=True)
    while capacity != 0 and weights != []:
        item_index = ratios.index(max(ratios))
        max_ratio = ratios.pop(item_index)
        weight = weights[item_index]
        del weights[item_index]
        if weight <= capacity:
            value += max_ratio * weight
            capacity -= weight
        else:
            value += max_ratio * capacity
            capacity = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    # a = input("enter info: ")
    # b = a.split()
    # b = [int(i) for i in b]
    # n = b[0]
    # capacity = b[1]
    # values = b[2:(2 * n + 2):2]
    # weights = b[3:(2 * n + 2):2]
    # print(get_optimal_value(capacity, weights, values))
