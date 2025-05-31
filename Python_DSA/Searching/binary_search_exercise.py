import time
import random

"""Binary Searching in Python"""
"""Example 1 : Calculate Total time taken to find element using Linear and Binary Search"""
def linear_searching(arr,target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

def binary_searching(arr, target):
    low=0
    high=len(arr)-1
    while low <= high:
        mid=(low+high)//2 # take midle element as mid
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1 # shift to right ->
        else:
            high = mid-1 # shift left <-
    return -1

size= 1_00_00_000
#print(type(data)) # int
data=list(range(size))  # data already sorted
target = data[size//2]

## Finding element using Linear searching method
start_time= time.time()
print(linear_searching(data,target))
end_time= time.time()
print(f"Total time taken to find element using Linear Search is {end_time-start_time :.6f} Seconds") #0.004001 Seconds

## Finding element using Linear searching method
start= time.time()
print(binary_searching(data,target))
end= time.time()
print(f"Total time taken to find element using Binary Search is {end-start :.6f} Seconds")
## here speed of execution of binary search is very fast in microseconds, and time module can calculate time for miliseconds
## this is reason we are getting execution time 0.00000 seconds for this code.

## to calculate we can use time.perf_counter()
start= time.perf_counter()
print(binary_searching(data,target))
end= time.perf_counter()
print(f"Total time taken to find element using Binary Search is {end-start :.6f} Seconds") #0.000017 Seconds

def binary_serach_using_recursion(arr, number_to_find,left_index, last_index):
    if left_index > last_index:
        return -1
    mid_index=(left_index+last_index)//2
    mid_number=arr[mid_index]

    if mid_number == number_to_find:
        return mid_number
    elif mid_number < number_to_find:
        left_index =mid_index+1
    else:
        last_index = mid_index - 1
    return binary_serach_using_recursion(arr, number_to_find,left_index, last_index)

print(f"Finding element using recursion : ")
start_t=time.perf_counter()
print(binary_serach_using_recursion(data, target, 0, len(data) - 1))
end_t=time.perf_counter()
print(f"Total Time taken to Finding element using recursion is : {end_t-start_t:.6f} Seconds") #0.000025 Seconds

"""
We can see for find same element within 1_00_000 entries time difference between linear search and binary search
from 1 Lakh element
Linear Search takes : 0.004001 Seconds
Binary Search takes : 0.000017 Seconds
Binary using Recusion Search Takes: 0.000025 Seconds

from 10 Lakh element
Linear Search takes : 0.046177 Seconds
Binary Search takes : 0.000019 Seconds

from 1 crore element
Linear Search takes : 0.515383 Seconds
Binary Search takes : 0.000048 Seconds
"""

""" 
What if list is empty
"""

arr=[]
target2=8
print(binary_searching(arr,target2)) # -1 element not found

"""
Calculate how many times number appears in sorted list with duplicates
"""
"""By Binary Search, we will create two seprate method first to find first accurance and other to last accurance
We'll use two modified binary searches:
One to find the first occurrence of the number
One to find the last occurrence
last_index - first_index + 1
"""
def first_occurance(arr, target):
    low =0
    high=len(arr)-1
    result = -1 # default if not found
    while low <= high:
        mid= (high+low)//2
        if arr[mid]==target:  # ind middle of page
            result=mid   # Found it!
            high = mid-1 # keep looking left for first occurance
        elif arr[mid] < target:
            low=mid+1 # Go right
        else:
            high = mid-1 # Go Left
    return result

def last_occurance(arr, target):
    low =0
    high=len(arr)-1
    result = -1
    while low <= high:
        mid= (high+low)//2
        if arr[mid]==target:
            result=mid
            low = mid+1 # keep looking right for last occurance
        elif arr[mid] < target:
            low=mid+1 # Go right
        else:
            high = mid-1 # Go left
    return result


def count_occurance(arr, target):
    first= first_occurance(arr,target)
    if first ==-1:
        return 0
    last=last_occurance(arr,target)
    return last - first+1
    """It count last - first +1 = total number of appearance. """
## Linear approch

def linear_approach(arr, target):
    return sum(1 for x in arr if x == target)

arr3=[2,5,7,53,55,77,55,77,2,5]
arr3=sorted(arr3)
target=77
#print(arr3) [2, 2, 5, 5, 7, 53, 55, 55, 77, 77]

print(linear_approach(arr3,target)) #2
print(count_occurance(arr3, target)) #2

dataa=[2, 2, 5, 6, 7, 7, 7, 66, 77, 77]
print(last_occurance(dataa,7))


