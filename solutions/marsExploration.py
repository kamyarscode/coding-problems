#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    # divide string into chunks of 3, check if string matches "sos" reference
    # pattern, if not add how many letters are wrong. 
    mismatch_value = 0
    ref_string = "SOS"
    divided_str = [s[i:i+3] for i in range(0, len(s), 3)]
    for substring in divided_str:
        for i in range(min(len(ref_string), len(substring))):

            if ref_string[i] != substring[i]:
                mismatch_value += 1  
    
    return mismatch_value
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
