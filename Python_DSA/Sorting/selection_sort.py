def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                print(f"Swap  happend {arr[j]} and {arr[min_index]} so min_index value become {min_index}")
                min_index = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"loop end Swap  happend {arr[i]} and {arr[min_index]} so min_index value become {min_index}")

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)  # Output: [11, 12, 22, 25, 64]
