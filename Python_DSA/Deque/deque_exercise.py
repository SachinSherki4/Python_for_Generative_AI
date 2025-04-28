
from collections import deque

# Adding itemd in deque
dq=deque()
dq.append(1)
dq.append(2)
dq.appendleft(3)
print(dq)  #deque([3, 1, 2])

# pop removing item from deque
print(dq.pop()) #2 last one (from right)
print(dq.popleft()) #3 from left

#Adding multiple items
dq.extend([1,64,6,7]) #start adding at last from 1st item
print(dq)  #deque([1, 1, 64, 6, 7])
dq.extendleft([6,8,4,3]) # start adding item at start from last item.
print(dq) #deque([3, 4, 8, 6, 1, 1, 64, 6, 7]) here items added in reverse manner
#input 6,8,4,3 => output order : 3, 4, 8, 6



