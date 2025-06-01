"""
HackerRank Question : https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9
The left-to-right diagonal = .
The right-to-left diagonal = .
Their absolute difference is .

Function description

Complete the  function with the following parameter:

: a 2-D array of integers
Return

: the absolute difference in sums along the diagonals
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Sample Input

STDIN      Function
-----      --------
3           arr[][] sizes n = 3, m = 3
11 2 4     arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: .

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal:
Difference:

Note: |x| is the absolute value of x.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    print(arr)
    primary_diagonal=0
    secondary_diagonal=0
    for i in range(len(arr)):
        primary_diagonal += arr[i][i]
        secondary_diagonal +=arr[i][n-i-1]
        #print(f"i value {i} Pimary Diagonal become : {primary_diagonal} and Secondary Diagonal become {secondary_diagonal} by adding {arr[i][n-i-1]}")
        return abs(primary_diagonal-secondary_diagonal)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
