#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_num = 0
    neg_num = 0
    zeros = 0
    array_size = len(arr)
    
    # Check for numbers that are positive, negative, or 0. Append to their
    # respective array.
    for number in arr:
        if number < 0:
            neg_num += 1
        elif number > 0:
            pos_num += 1
        else:
            zeros += 1
    
    print (f'{pos_num/array_size:.6f}')
    print (f'{neg_num/array_size:.6f}')
    print (f'{zeros/array_size:.6f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)