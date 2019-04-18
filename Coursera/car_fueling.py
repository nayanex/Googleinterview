# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refill = 0
    current_refill = 0

    stops.append(distance)
    
    n = len(stops) - 1

    if (tank >= distance):
        return 0

    while (current_refill < n):
        last_refill = current_refill
        
        while(current_refill < n and stops[current_refill + 1] - stops[last_refill] <= tank):
            current_refill = current_refill + 1
        
        if current_refill == last_refill:
            return -1

        if stops[current_refill] <= distance :
            num_refill = num_refill + 1
        print(cu)        
    return num_refill

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
