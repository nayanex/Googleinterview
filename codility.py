# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    smallest_pos_int = A[-1]
    A.sort()
    max_el = max(A)
    
    if max_el <= 0:
        return 1
        
    for elem in range(1, max_el + 1):
        if elem not in A:
            return elem

    return max_el + 1