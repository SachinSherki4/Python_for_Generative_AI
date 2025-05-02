
def insertion_sort(arr):
    # Start from second element
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are > current
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]  # Shift right
            j -= 1
        arr[j + 1] = current  # Insert at correct spot

arr = [5, 3, 4, 1]
insertion_sort(arr)
print(arr)  # Output: [1, 3, 4, 5]
