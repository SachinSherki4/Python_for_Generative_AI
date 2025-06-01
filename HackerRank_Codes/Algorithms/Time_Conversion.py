"""
HackerRank Question : https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the  function with the following parameter(s):

: a time in  hour format
Returns

: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input 0

07:05:45PM
Sample Output 0

19:05:45
"""

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
#

def timeConversion(s):
    # Write your code here
    time = s.split(":")
    hour = time[0]
    if hour[0] == 0:
        hour = int(hour[1])
        print(f"{hour} first")
    else:
        hour = int(hour) % 12
        print(f"{hour} seconds")
    minute = time[1]
    seconds = time[2]
    if "AM" in seconds:
        if len(str(hour)) == 1:
            hour = str(hour)
            hour = "0" + hour
        else:
            hour = str(hour)
        return (hour + ":" + minute + ":" + seconds[0:2])
    elif "PM" in seconds:
        hour += 12
        return (str(hour) + ":" + minute + ":" + seconds[0:2])
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

    # fptr.write(result + '\n')
    #
    # fptr.close()
