#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here

    sorted_array = sorted(arr)
    array_length = len(sorted_array)
    subs = []
    smallest_diff = float('inf')
    print (sorted_array)
    for i in range(0, array_length-2+1):
        abs_smallest = abs(sorted_array[i+1] - sorted_array[i])
        
        if  abs_smallest < smallest_diff:
            smallest_diff = abs_smallest
            
            subs = sorted_array[i:i+2]
        
        elif abs_smallest == smallest_diff:
            subs.extend(sorted_array[i:i+2])
            
    return subs
                        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
