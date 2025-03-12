#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    sorted_array = sorted(arr)

    array_length = len(sorted_array)
    smallest_diff = float('inf')
    for i in range(0, array_length-2+1):
        abs_smallest = abs(sorted_array[i+1] - sorted_array[i])
        
        if  abs_smallest < smallest_diff:
            smallest_diff = abs_smallest
            
    return smallest_diff
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
