"""
HackerRank Question : https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
Staircase detail

This is a staircase of size :

   #
  ##
 ###
####
Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

Function Description

Complete the  function with the following parameter(s):

: an integer
Print

Print a staircase as described above. No value should be returned.
Note: The last line is not preceded by spaces. All lines are right-aligned.

Input Format

A single integer, , denoting the size of the staircase.

Constraints

 .

Sample Input

6
Sample Output

     #
    ##
   ###
  ####
 #####
######
Explanation

The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .

"""
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

"""
     #
    ##
   ###
  ####
 #####
######
"""
def staircase(n):
    print("staircase : ")
    # Write your code here
    for i in range(0, n):
        print(((n - i - 1) * " ") + ((i + 1) * '#'))

"""
*
**
***
****
*****
"""
def right_half(n):
    print("right_half : ")
    for i in range(0,n):
        print(((i+1)*'#')+((n-i-1)*" "))


"""
*****
****
***
**
*
"""
def inverted_right_half(n):
    print("inverted_right_half : ")
    for i in range(0,n):
        #print(i)
        print(((n-i)*'#')+((i)*" "))

"""
*****
 ****
  ***
   **
    *
"""

def inverted_left_half(n):
    print("inverted_left_half : ")
    for i in range(0,n):
        print(((i)*" ")+((n-i)*'#'))

""" Full Pyramid
    *
   ***
  *****
 *******
*********
"""
def full_pyramid(n):
    print("full_pyramid : ")
    for i in range(0,n):
        print(('#'*(i*2+1)).center(n*2," "))

""" inverted_full_pyramid
*********
 *******
  *****
   ***
    *
"""

def inverted_full_pyramid(n):
    print("inverted_full_pyramid : ")
    for i in range(0,n):
        print((' '*i)+('*'*((n-i)*2-1))+(' '*i))

"""half Diamond star pattern
*
**
***
****
*****
******
*****
****
***
**
*

"""

def half_diamond_pyramid(n):
    print("half_diamond_pyramid : ")
    for i in range(0,n):
        print(('*'*(i+1))+((n-i)*" "))
    for i in range(0,n):
        print(('*'*(n-i-1))+(" "*(i)))

""" Diamond Shape
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
"""
def diamond_shape(n):
    print("Diamond Shape : ")
    for i in range(1,n+1):
        print(" "*(n-i)+"* "*i)
    for i in range(n,0,-1):
        print(" "*(n-i)+"* "*i)





if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
    right_half(n)
    inverted_right_half(n)
    inverted_left_half(n)
    full_pyramid(n)
    inverted_full_pyramid(n)
    half_diamond_pyramid(n)
    diamond_shape(n)


