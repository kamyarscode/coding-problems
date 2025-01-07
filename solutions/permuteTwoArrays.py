#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # Write your code here
    """
    'For each query, return YES if some permutation A', B' satisfying the relation exists. Otherwise, return NO.' is confusing as its asking for ANY permutation of the arrays matching the A'[i] + B'[i] >= k. This means a simple if statement can check if theres one instance of truth, but the real solution accepted checks if ALL permutations give you something >= k. Theres also an error in the 'explanation' where A[0] + B[1] should be A[0] + B[0].
    
    """
    
    # Don't compute if len isn't same for both arrays.
    if len(A) != len(B):
        return 'NO'
    
    # Sorting maximizes sums at every pair. this gives you likely chance 
    A.sort(reverse=True)
    B.sort()
    
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"

    return "YES"
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
