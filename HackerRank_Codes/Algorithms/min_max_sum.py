"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

16 24
Function Description

Complete the  function with the following parameter(s):

: an array of  integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.No value should be returned.

Note For some languages, like C, C++, and Java, the sums may require that you use a long integer due to their size.

Input Format

A single line of five space-separated integers.

Constraints


Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

The numbers are , , , , and . Calculate the following sums using four of the five integers:

Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Hints: Beware of integer overflow! Use a 64-bit integer to store the sums.

Need help to get started? Try the Solve Me First problem.

"""



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
    # Write your code here
    sum_amount = []
    total_sum = sum(x for x in arr)
    for i in arr:
        remaining_sum = total_sum - i
        sum_amount.append(remaining_sum)
    print(min(sum_amount), max(sum_amount))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
