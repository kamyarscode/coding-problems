#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
def maxMin(k, arr):
    # Sort array and create array for unfairness values.
    arr.sort()
    unf_array = []

    # Create sliding window so you look at chunk sizes of k.
    for i in range(len(arr) - k + 1):
        # Since the array is sorted, the first value in the sliding window, the first value below is the max and the second value is the min.
        # Through this, we can essentially replace max() - min().
        # Append unfairness values to this array. 
        unf_array.append(arr[i+k-1] - arr[i])
        
    # Return the minimum value in the array.
    return min(unf_array)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
