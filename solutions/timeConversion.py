#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
    
def timeConversion(s):
    # Write your code here

    # Split the array into hour:minute:second
    split_time = s.split(':')
    
    hour = split_time[0]
    minute = split_time[1]
    second = split_time[2]

    # Look for AM or PM in the seconds string. If PM and time is 12, leave it alone. If not, then add 12. 
    if 'PM' in second:
        second = second.replace('PM', '')

        if hour == "12":
            hour = hour
            
        else:
            hour = str(int(hour) + 12)

    # If AM, leave the time alone completely.
    if 'AM' in second:
        second = second.replace('AM', '')

        if hour == "12":
            hour = "00"
    
    # Combine and return value.
    combined_str = hour + ":" + minute + ":" + second
    
    return combined_str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
