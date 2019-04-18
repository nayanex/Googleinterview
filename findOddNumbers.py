#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findNumber function below.
def findOddNumbers(left, right):
    
    if left%2 !=0:
        lower = left
    else:
        lower = left + 1

    if right%2 !=0:
        upper = right
    else:
        upper = right - 1

    return list(range(lower, upper + 1, 2))

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]

    print(findOddNumbers(input_numbers[0], input_numbers[1]))
