
## Deque in python
1. deque stand for duoble-ended queue.
2. It is high performance data structre allow append(adding) and pop(removing) items from both ends (right and left)
3. Compare to list : list append() and pop() from end are fast (O(1)).
4. But list.insert(0,item) at begenning are slow
5. deque make insertion or deletion at either end very fast.
6. Syntax : dq= deque(iterable) : iterable : list, tuple, string, etc

## Basic Methods
1. deque.append(x), deque.appendleft(x)  : add item
2. pop(), popleft() : remove item
3. extend(iterable), extendleft(iterable) : add multiple items
4. rotate(n) : rotate element n step to right(or left if n is negative).

## Real AI/ML/Data Science/GenAI Work
1. Situation : Sliding Window Algorithms
    1. Why deque Helps : Maintain a moving window efficiently
    2. Real-world Example  : Moving average, NLP N-grams
2. Situation : Task Scheduling
    1. Why deque Helps : Queue tasks dynamically
    2. Real-world Example  : Processing batch jobs
3. Situation : BFS in Graphs
    1. Why deque Helps : Breadth-First Search uses queue
    2. Real-world Example  : AI search algorithms
4. Situation : Streaming Data Processing
    1. Why deque Helps : Consume, process and rotate live data
    2. Real-world Example  : Log ingestion, online learning
5. Situation : Rate-limiting / Cooldowns
    1. Why deque Helps : Track recent requests
    2. Real-world Example  : API throttling, real-time systems

[Solutions](deque_exercise.py)

## Mini Projects

1. Project 1: IoT Sensor Network – Smart Room Temperature Alert System
1. Step-by-Step Plan:
   1. Simulate real-time temperature sensor readings.
   2. Use a sliding window with deque to track recent values.
   3. Calculate average, detect if new reading is >20% deviation.
   4. Raise alerts in real-time.

