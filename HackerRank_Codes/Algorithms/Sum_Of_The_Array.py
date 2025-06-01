
"""
HackerRank Question : https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true

Given an array of integers, find the sum of its elements.

For example, if the array , , so return .

Function Description

Complete the  function with the following parameter(s):

: an array of integers
Returns

: the sum of the array elements
Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers representing the array's elements.

Constraints


Sample Input

STDIN           Function
-----           --------
6               ar[] size n = 6
1 2 3 4 10 11   ar = [1, 2, 3, 4, 10, 11]
Sample Output

31
Explanation

Print the sum of the array's elements: .
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    sum=0
    for i in range(0,len(ar)):
        sum += ar[i]
    return sum
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
