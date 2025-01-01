#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

# Use collections counter method. Counter method is needed since occurrences(frequency) need to be tracked, it is not a simple array comparison (brr - arr)
# to see missing values. 
# Counter method
from collections import Counter

def missingNumbers(arr, brr):
    # Write your code here
    # Get array occurrences.
    arr_counter = Counter(arr)
    brr_counter = Counter(brr)

    # Calculate differences and sort.
    diff = sorted(brr_counter - arr_counter)
    
    return diff

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
