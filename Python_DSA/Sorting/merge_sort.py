import random
import time
from typing import List, Tuple

## Exercise 1. Sort array [3,6,22,8,4,2]
def merge_sort(arr):
    if len(arr) <= 1:
        return arr # it is already sorted


    mid=len(arr)//2 # center
    left = merge_sort(arr[:mid])  # left array
    right = merge_sort(arr[mid:]) ## right array
    return merge_sort_with_customer_kay(left, right)

def merge(left,right):
    sorted_array=[]
    i=j=0
    ## merge element from both list in sorted ordered.
    while i<len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i +=1
        else:
            sorted_array.append(right[j])
            j +=1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

numbers=[3,6,22,8,4,2]
#print(merge_sort(numbers))


## Exercise 2. Merge sort on a list of tuple
tuple1=[(1,3),(4,1),(3,2),(2,4)]

def tuple_merge(tuple_list):
    if len(tuple_list) <= 1:
        pass

def sort_tutple(left, right):
    sorted_tutple=()
    i=j=0
    if i <len(left) and j <len(right):
        pass

def merge_sort_with_customer_kay(left: List, right : List, key=lambda x :x) -> List :
    result=[]
    i=j=0
    while i <len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
           result.append(left[i])
           i +=1
        else:
            result.append(right[j])
            j +=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

## Exercse 3. Performeance benchmark with large data set
#number_list= [random.randint(0,100000) for _ in range(1_00_00_000)]
start= time.perf_counter()
#sorted_list = merge_sort(number_list)
end =time.perf_counter()
#print(f"Total tim taken by merge sort to sort 1 Lakh numbers is {end - start :.6f} Seconds") # 0.300111 Seconds
print(f"Total tim taken by merge sort to sort 1 Crore numbers is {end - start :.6f} Seconds") # 54.034857 Seconds

neste_list= [[random.randint(1,555) for _ in range(3)] for _ in range(3)]
print(neste_list) # [[219, 278, 344], [525, 269, 152], [542, 348, 421]]

print(f"Sorted Nested List : {merge_sort(neste_list)}")
