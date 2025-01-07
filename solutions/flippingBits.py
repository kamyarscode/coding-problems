#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Use dictionary lookup
    b_dict = {'0': '1', '1': '0'}
    unsigned = ""
    
    # 2 ways to convert to binary. 
    #binary_value = format(n, '032b')
    binary_value = f'{n:032b}'

    # Inverse bits
    for bit in binary_value:
        unsigned += b_dict[bit]
    
    # Convert back to int
    return int(unsigned, 2)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
