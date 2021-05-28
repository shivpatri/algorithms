# Uses python3
import sys
def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    for i in range(len(weights)-1, -1, -1):
        if weights[i] == 0:
            value += values[i]
            values.pop(i)
            weights.pop(i)
    ratios = [i / j for i, j in zip(values, weights)]
    sort_order = sorted(range(len(ratios)), key=ratios.__getitem__, reverse=True)
    i = 0
    while capacity > 0 and i < len(weights):
        portion = min(capacity, weights[sort_order[i]])
        value += portion*ratios[sort_order[i]]
        capacity -= portion
        i = i + 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))