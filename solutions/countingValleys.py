#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Solve using stack.
    
    # elevation_stack = []
    # valley = 0
    
    # for step in path:
    #     if step == "D":
    #         elevation_stack.append(step)
    #     elif step == "U":
    #         if elevation_stack:
    #             elevation_stack.pop()
    #         if not elevation_stack:
    #             valley += 1
    # return valley
    
    elevation = 0
    valley_count = 0
    
    for step in path:
        if step == "U":
            elevation += 1
            if elevation == 0:  # Return to sea level
                valley_count += 1
        elif step == "D":
            elevation -= 1
    
    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
