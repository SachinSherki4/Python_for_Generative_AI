
"""
Name          : Sub-Array Divison
Category      : Implementation
Difficulty    : Easy
Language      : Python3
Question Link : https://www.hackerrank.com/challenges/the-birthday-bar/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    highest_record=scores[0]
    lowest_record=scores[0]
    highest_count=0
    lowest_count=0
    for score in scores:
        if score > highest_record:
            highest_record=score
            highest_count +=1
        elif score < lowest_record:
            lowest_record =score
            lowest_count +=1
        else:
            continue
    return highest_count, lowest_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
