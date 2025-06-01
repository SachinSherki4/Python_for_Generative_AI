"""
Name          : Grading Students
Category      : Implementation
Difficulty    : Easy
Language      : Python3
Question Link : https://www.hackerrank.com/challenges/grading/problem

"""

# !/bin/python3

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
    def gradingStudents(grades):
        final_grades = []
        for grade in grades:
            if grade < 38:
                final_grades.append(grade)
            else:
                next_multiple = ((grade // 5) + 1) * 5
                print(next_multiple)
                if next_multiple - grade < 3:
                    final_grades.append(next_multiple)
                else:
                    final_grades.append(grade)
        return final_grades
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #print(6 % 5)
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    #
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
