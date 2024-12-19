#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    # Set default values
    min_value = 0
    max_value = 0
    
    # Sort the array
    sorted_array = sorted(arr)

    # Basic abstract solution.
    min_value = sum(sorted_array[0:len(sorted_array)-1])
    max_value = sum(sorted_array[::-1][0:len(sorted_array)-1])


    print (min_value, max_value)        

# Alternate solution more hands on.
def miniMaxSumAlternate(arr):

    # Set default values
    min_value = 0
    max_value = 0
    
    # Sort the array
    sorted_array = sorted(arr)

    # For most minimum, we need to include the smallest entry in the array up to len-1 (in our case, the array len is always 5.)
    for number in sorted_array[0:len(sorted_array)-1]:
        min_value += number
    
    # For maximum value, we exclude the smallest value. We can reverse the sorted string then run it from the 0 index to the len-1.
    for number in sorted_array[::-1][0:len(sorted_array)-1]:
        max_value += number
        
    
    print (min_value, max_value)        
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
