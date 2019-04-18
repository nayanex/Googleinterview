# Uses python3
import sys

def get_change(m):
    min_coins = 0
    remainder = m

    if m > 10:
        remainder = m % 10
        min_coins += m // 10
    
    if remainder != 0:
        min_coins += (remainder // 5) + (remainder % 5)

    return min_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
