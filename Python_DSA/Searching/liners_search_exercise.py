
def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

nums = [10, 20, 30, 40, 50]
target = 30
result=linear_search(nums,target)
print(f"Found at index : {result}") #Found at index : 2