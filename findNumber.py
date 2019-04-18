#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findNumber function below.
def findNumber(arr, k):
    arr = arr.sort()
    n = len(arr)
    for index in range(n-1):
        if k == arr[index]:
            return 'YES'
    return 'NO'

def split(input_list):
    """
    Splits a list into two pieces
    :param input_list: list
    :return: left and right lists (list, list)
    """
    input_list_len = len(input_list)
    midpoint = input_list_len // 2
    return input_list[:midpoint], input_list[midpoint:]

