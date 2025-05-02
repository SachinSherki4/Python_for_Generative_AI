## *Sorting in Python*

---
## *Bubble Sort*
1. It is simplest sorting technique use to sort the sequence, list, array
2. Two adjecent element are compared and swapper in correct ordered.
3. Time complexity(wors if element list is not sorted)
4. Good for Teaching, debugging, simulations

```commandline
Pass 1:
[5, 1, 4, 2, 8]
 → compare 5 and 1 → swap → [1, 5, 4, 2, 8]
 → compare 5 and 4 → swap → [1, 4, 5, 2, 8]
 → compare 5 and 2 → swap → [1, 4, 2, 5, 8]
 → compare 5 and 8 → no swap → [1, 4, 2, 5, 8]
Pass 2:
 → keep bubbling...
Eventually: [1, 2, 4, 5, 8]
```
```commandline
📈 Time & Space Complexity:
Case	Time
Best	O(n) ✅ (when already sorted + optimized)
Worst	O(n²)
Space	O(1) ✅ (in-place)
```

## *Selection Sort*
1. It is simple sorting algorithm where list is devided into two parts.
2. sorted part(built from left)
3. Unsorted Part (rest of the list)

> *How it works*
> 1. Start from the beginning of the list.
> 2. Find the minimum element in the unsorted part.
> 3. Swap it with the first unsorted element.
> 4. Repeat for the next position until the whole list is sorted.

```commandline
Pass 1: Find min in [5, 2, 4, 1] → 1 → Swap with 5 → [1, 2, 4, 5]
Pass 2: Find min in [2, 4, 5] → 2 → No swap
Pass 3: Find min in [4, 5] → 4 → No swap
```

```commandline
📈 Time & Space Complexity:
Case	Time
Best	O(n²)
Worst	O(n²)
Space	O(1) ✅ in-place
```
> *Use Cases*
> 1. Selection Sort is not used in high-performance applications, but it's powerful fo
> 2. Learning and debugging
> 3. Simulating decision-making logic
> 4. Teaching algorithmic thinking


## *Insertion Sort*
1. Insertion Sort is a simple sorting algorithm that works like how you sort playing cards in your hand:
2. One by one, you pick an element from the unsorted part
3. And insert it in the correct position in the sorted part on the left

> 🧠 Concept:
> 1. Start from the second element.
> 2. Compare it with the elements before it.
> 3. Shift larger elements to the right.
> 4. Insert the current element at the correct spot.

```commandline
Initial list: [5, 3, 4, 1]

Pass 1: 3 < 5 → move 5 right → [3, 5, 4, 1]
Pass 2: 4 < 5 → move 5 right → insert 4 → [3, 4, 5, 1]
Pass 3: 1 < all → shift all and insert → [1, 3, 4, 5]
```






