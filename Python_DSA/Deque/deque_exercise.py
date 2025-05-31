
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

#RRotate using data.rotate(n)
data=deque([2,5,8,4,1])
print(data) #deque([2, 5, 8, 4, 1])
data.rotate(2)
print(data) #deque([4, 1, 2, 5, 8]) last two come forword
data.rotate(-1)
print(data) #deque([1, 2, 5, 8, 4]) - first one go to last position

"""Time-Task scheduler"""
task=["Task-A", "Task-B", "Task-C", "Task-D"]
task_data=deque(task)
for time_slot in range(6):
    print(f"Time Slot : {time_slot+1} : {task_data[0]}")
    task_data.rotate(-1) # send first entry to last

"""
Time Slot : 1 : Task-A
Time Slot : 2 : Task-B
Time Slot : 3 : Task-C
Time Slot : 4 : Task-D
Time Slot : 5 : Task-A
Time Slot : 6 : Task-B
"""

