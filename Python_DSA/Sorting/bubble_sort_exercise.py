

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Optimization: track if any swaps happened
        for j in range(0, n - i - 1):  # last i elements are already sorted
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # List is sorted already

nums = [5, 1, 4, 2, 8]
bubble_sort(nums)
print(nums)  # Output: [1, 2, 4, 5, 8]
