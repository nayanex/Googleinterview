# Uses python3
def calc_fib(n):
    fib = []
    fib.append(0)
    fib.append(1)
    
    if n < 2:
        return fib[n]
    
    for index in range(2,n+1):
        fib.append(fib[index-1] + fib[index-2])

    return fib[n]

n = int(input())
print(calc_fib(n))
