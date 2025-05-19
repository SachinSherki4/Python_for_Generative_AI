### Stacks in Python
1. Stacks in python refers to DS, Last In First Out data Structure.

### Python Stack Implementation
1. Using List : (simple but not efficient for large-scale popping)

```commandline
stack = []
stack.append(10)  # Push
stack.append(20)
print(stack.pop())  # Pop → 20
```
2. Using collections.deque (fast and efficient)
```commandline
from collections import deque
stack = deque()
stack.append(10)
stack.append(20)
print(stack.pop())  # Output: 20
```
3. Queue in Python (FIFO: First-In, First-Out)
```commandline
queue = []
queue.append(10)
queue.append(20)
print(queue.pop(0))  # Output: 10
```
4. Using deque (efficient)
```commandline
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
print(queue.popleft())  # Output: 10
```
5. Priority Queue / Heap (heapq) : A priority queue allows the smallest element to be removed first.
```commandline
import heapq

pq = []
heapq.heappush(pq, 5)
heapq.heappush(pq, 1)
heapq.heappush(pq, 3)

print(heapq.heappop(pq))  # Output: 1
Under the hood, it uses a binary heap → Time complexity: Push/POP : O(log n)
```
