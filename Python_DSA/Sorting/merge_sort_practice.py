

def merge(left, right):
    sorted_array=[]
    i=j=0
    # i starting from 0 and len() start from 1 so less than sign this will compare only if both condition satisfied
    # It one array end, comparision ends, it will break and add leftover element directly to sorted array
    # as if function receive array len() > 1 it will always in sorted manner.
    while i < len(left) and j <len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i +=1
        else:
            sorted_array.append(right[j])
            j +=1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

def merge_sort(arr):
    if len(arr) <=1:
        return arr # as it is already in sorted manner.

    mid= len(arr)//2 #
    left = merge_sort(arr[:mid]) # again sort all left region
    right = merge_sort(arr[mid:])
    return merge(left, right)

arr=[2,7,3,7,31,2]
print(merge_sort(arr))