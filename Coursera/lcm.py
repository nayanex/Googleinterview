# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

# greatest common divisor
def gcd(a, b):
    greater = max(a, b)
    smaller = min(a, b)

    if smaller == 0:
        return greater

    remainder = greater % smaller
    
    return gcd(smaller, remainder)

# least common divisor
def lcm(a, b):
    return a*b//gcd(a,b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

