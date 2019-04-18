# Uses python3
import sys

WEIGHT = 1
VALUE_PER_WEIGHT = 0

def get_optimal_value(capacity, weights, values):
    value = 0.
    
    value_per_weight = [v / float(w) for v, w in zip(values, weights)]

    value_per_weight_tuples = sorted(zip(value_per_weight, weights), reverse=True)

    for item_tuple in value_per_weight_tuples:
        if capacity == 0:
            return value
        to_fill = min(item_tuple[WEIGHT], capacity)
        value += to_fill*item_tuple[VALUE_PER_WEIGHT]
        capacity -= to_fill
        
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


    
