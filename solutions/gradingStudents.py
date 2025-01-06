#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    # Create new output array
    out_grades = []
    for grade in grades:
        if grade >= 38:
            
            # Find the next multiple of 5 rounded up. 
            multiple_of_five = 5 * math.ceil(grade / 5)
            # Input logic here for rounding
            if multiple_of_five - grade < 3:
                out_grades.append(multiple_of_five)
                
            if multiple_of_five - grade >= 3:
                out_grades.append(grade)

        else:
            out_grades.append(grade)
            
    return out_grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
