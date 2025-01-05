#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here

    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    chars = [i.lower() for i in s]
    
    if all(item in chars for item in alphabet_lower):
        return "pangram"

    return "not pangram"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
