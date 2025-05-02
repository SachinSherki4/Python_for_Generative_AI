### *Seaching in Python*

---
### *Linear Search*
1. It is simple search algorithm
2. It goes one-by one throught list or sequence.
3. Stops when found element or reach end.

```commandline
Given: list : [3, 8, 1, 5, 9], target = 5

Check list[0] → 3 → not 5  
Check list[1] → 8 → not 5  
Check list[2] → 1 → not 5  
Check list[3] → 5 → ✅ Found at index 3
```
### *📈 Time Complexity*
1. Worst-case: O(n) = dont know the exact location
2. Best-case: O(1) if the item is at the start
3. Space Complexity: O(1)

### *Binary Search*
1. It is efficient algorithm to find an element in a sorted array/list.
2. It works  by repeatedly dividing the search space into a half.

```commandline
low = 0 : starting point
high=len(array) -1 : as array index start from 0
mid = (low+high)//2 : get mid integer  only
```

## Examples 
1. Calculate Total time taken to find element using Linear and Binary Search.
2. We can see for find same element within 1_00_000 entries time difference between linear search and binary search
3. Calculate how many times number appears in sorted list with duplicates.


[Linear_Searching_Solutions](liners_search_exercise.py)
[Binary_Searching_Solutions](binary_search_exercise.py)
