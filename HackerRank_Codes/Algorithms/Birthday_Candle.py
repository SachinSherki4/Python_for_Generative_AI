
"""
HackerRank Question : https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
You are in charge of the cake for a child's birthday. It will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Your task is to count how many candles are the tallest.

Example


The tallest candles are 4 units high. There are 2 candles with this height, so the function should return 2.

Function Description

Complete the function  with the following parameter(s):

: the candle heights
Returns

: the number of candles that are tallest
Input Format

The first line contains a single integer, , the size of .
The second line contains  space-separated integers, where each integer  describes the height of .

Constraints

Sample Input 0

4
3 2 1 3
Sample Output 0

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    max_candle=max(candles)
    print(max_candle)
    count=sum(1 for x in candles if x==max_candle)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
