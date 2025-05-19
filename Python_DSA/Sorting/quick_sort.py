import  random
import time
import pprint
import string
def quick_sort(arr, key=lambda x :x ):
    if len(arr) <=1: # already sorted if have only one element
        return arr
    pivot=arr[0] # take first element as pivot
    left = [ x for x in arr[1:] if x < pivot] # add all element in left which are less that pivot
    right = [x for x in arr[1:] if x >= pivot]  # add all element to right which are equal or more greater than pivot
    return quick_sort(left) + [pivot] + quick_sort(right) # Now use recursion to sort both left and right array with center as pivote array element

## Exercise 1. Sort list of number using Quick Sort
numers=[55,44,12,45,11,1,74,8,66,44]
print(f"Sorted List based on Quick Sort Algorithm : {quick_sort(numers)}")  #[1, 8, 11, 12, 44, 44, 45, 55, 66, 74]

## Exercise 2. Sort large set of data using quick sort and calculate time

data_set=[random.randint(1,1000) for _ in range(1_00_000)]
start=time.perf_counter()
#result=quick_sort(data_set)
end=time.perf_counter()
print(f"Total Time taken to sort 1 Lakh data using quick sort is {end - start :.6f} Seconds") #1.1541 Seconds
print(f"Total Time taken to sort 1 Crore data using quick sort is {end - start :.6f} Seconds") # > than 1 minutes


def quick_sort_student_data(arr):
    if len(arr) <=1: # already sorted if have only one element
        return arr
    pivot=arr[0] # take first element as pivot
    left = [ x for x in arr[1:] if x['Score'] < pivot['Score']] # add all element in left which are less that pivot
    right = [x for x in arr[1:] if x['Score'] >= pivot['Score']]  # add all element to right which are equal or more greater than pivot
    return quick_sort_student_data(left) + [pivot] + quick_sort_student_data(right) # Now use recursion to sort both left and right array with center as pivote array element


## Exercse 3. Sort List of students based on score
student_data=[{"ID" :random.randint(1,100), "Name": ''.join(random.choices(string.ascii_lowercase,k=6)).capitalize(), "Score": random.randint(30,95)} for _ in range(10)]
pprint.pprint(student_data)

sorted_students= quick_sort_student_data(student_data)
pprint.pprint(f"Sorted Students based on Score uisng quick sort are \n{sorted_students}")




