#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    # subarray needs to be m
    # sum of values in subarray needs to be d
    
    count = 0
    subarray_len = len(s)
    window_stop = subarray_len - m # set value to stop at so you don't go over index size
    
    for i in range(0, window_stop + 1): #time complexity O(n)
    
        if sum(s[i:i+m]) == d: # make note this is exclusive, so index i+m is actually showing value i+m-1 in the array. 
            count += 1
                
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
