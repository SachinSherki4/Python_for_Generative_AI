
## Defaultdict dictionary in python Collections
1. Defaultdict is special dictionary provided by Collections module in python.
2. It automatically assign an default value when we try to access any missing key, when we try to access it,
3. no need to manually check key is present or not.
4. Regular dct- try to access missing key - KeyError
5. defaultdict : create on-the-fly key with default value.
6. Syntax : from collections import defaultdict
7. d=defaultdict(default_factory)  #default_factory : functions that provide default value like int, float, list

## Example 
1. Create defaultdict for int
2. defaultdict with list 

## Use Cases for AI/ML
1. AI/ML, Grouping data by categaries (eg, product data, product click, etc)
2. Gen AI — Token Frequency (e.g., word counts)
3. Data Science — Building Graphs : When building adjacency lists for graphs (recommendation systems, etc)
4. ML Pipelines — Grouping Model Metrics : When aggregating metrics from multiple experiments

[Solutions](defaultdict_exercise.py)

## Mini-Project : News Article Tagging (Multi-Label Classifier Preprocessing)
1. Developing a Multi-Label Classification System for a News Website
2. Each news article can belong to multiple categories ["Politics", "World", "Technology", "Health", etc.]

## 📦 Goal:
1. ✅ Build a tag-to-articles mapping: (Which articles belong to which tag?)
2. ✅ Handle missing tags safely without crashing.
3. ✅ Show count of how many articles per tag.
4. ✅ Prepare a reverse mapping: (For each tag, list of article titles.)


[Mini_project](mini_project_new_article_tagging.py)