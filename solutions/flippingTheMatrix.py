#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.

def flippingMatrix(matrix):
    # Write your code here.
    # Secondary solution for this problem
    # We still need to define coordinates:
    """
    coordinates:
    top left - [i][j]
    bottom left - [length - i - 1][j]
    top right - [i][length - j - 1]
    bottom right - [length - i - 1][length - j - 1]
    """
    matrix_len = len(matrix)
    max_sum = 0

    for i in range(matrix_len//2):
        for j in range(matrix_len//2):

            max_sum += max(
            max(matrix[i][j], matrix[i][matrix_len - j - 1]),
            max(matrix[matrix_len - i - 1][matrix_len - j - 1], matrix[matrix_len - i - 1][j]))

    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
