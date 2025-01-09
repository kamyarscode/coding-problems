#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    # Indeces:
    #0,0: 1,1: 2,2 - right
    #0,2: 1,1: 2,0 - left
    
    left_diag = 0
    right_diag = 0
    for i in range(len(arr)):
        print (i)
        left_diag += arr[i][i] # i can be same for left diag. Refer above.
        right_diag += arr[i][len(arr) - 1 - i];

    return abs(left_diag - right_diag)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
