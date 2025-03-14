#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here

    stick_sort = sorted(sticks, reverse=True)
    
    for i in range(0, len(stick_sort) - 2):
        if stick_sort[i] < stick_sort[i + 1] + stick_sort[i + 2]:
            triangle = [stick_sort[i], 
                    stick_sort[i + 1], 
                    stick_sort[i + 2]]
                    
            
            return sorted(triangle)

    return [-1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
