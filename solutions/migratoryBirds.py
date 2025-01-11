#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

from collections import Counter
def migratoryBirds(arr):
    # Write your code here
    
    bird_count = Counter(arr)

    # Create array of the most frequent bird's index.
    bird_sighting_min = [keys for keys, values in bird_count.items() if values == max(bird_count.values())]
    
    return min(bird_sighting_min)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
