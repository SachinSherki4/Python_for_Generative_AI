
from collections import defaultdict

#Example 1. Create defaultdict for int
d= defaultdict(int)
print(d['a']) #0 here dictionary d dont have key 'a' so it created at runtime
d['a'] +=1
print(d['a']) #1
print(d) #defaultdict(<class 'int'>, {'a': 1})

#Example 2. defaultdict with list
d=defaultdict(list)
d['fruits'].append("Mango")
d['fruits'].append("Grapes")
print(d) #defaultdict(<class 'list'>, {'fruits': ['Mango', 'Grapes']})

"""
## Use Cases for AI/ML
1. AI/ML, Grouping data by categaries (eg, product data, product click, etc)
2. Gen AI — Token Frequency (e.g., word counts)
3. Data Science — Building Graphs : When building adjacency lists for graphs (recommendation systems, etc)
4. ML Pipelines — Grouping Model Metrics : When aggregating metrics from multiple experiments
"""
#1. AI/ML, Grouping data by categaries (eg, product data, product click, etc)
user_clicks = [
    ('user1', 'product1'),
    ('user2', 'product2'),
    ('user1', 'product3')
]
click_map=defaultdict(list)
for user,product in user_clicks:
    click_map[user].append(product)
print(click_map) #{'user1': ['product1', 'product3'], 'user2': ['product2']})

#2. Gen AI — Token Frequency (e.g., word counts)
tokens = ['the', 'cat', 'sat', 'on', 'the', 'mat']
count=defaultdict(int)
for token in tokens:
    count[token] +=1
print(count) #{'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1})

#3. Data Science — Building Graphs : When building adjacency lists for graphs (recommendation systems, etc)
edges = [('A', 'B'), ('A', 'C'), ('B', 'C')]
graph=defaultdict(list)
for start, end in edges:
    graph[start].append(end)
print(graph) #{'A': ['B', 'C'], 'B': ['C']})

#4. ML Pipelines — Grouping Model Metrics : When aggregating metrics from multiple experiments
experiments = [
    ('model1', 'accuracy', 0.91),
    ('model1', 'f1_score', 0.88),
    ('model2', 'accuracy', 0.93)
]
matrix=defaultdict(dict)
for model, matric,value in experiments:
    matrix[model][matric]=value
print(matrix) #{'model1': {'accuracy': 0.91, 'f1_score': 0.88}, 'model2': {'accuracy': 0.93}})
