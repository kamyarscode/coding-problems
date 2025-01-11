#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    num_bool = True
    lower_bool = True
    upper_bool = True
    special_bool = True

    for char in password:
        if char in numbers:
            num_bool = False
        if char in lower_case:
            lower_bool = False
        if char in upper_case:
            upper_bool = False
        if char in special_characters:
            special_bool = False
            
    return max(num_bool + lower_bool + upper_bool + special_bool, 6 - n)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
