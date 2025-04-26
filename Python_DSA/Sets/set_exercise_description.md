
## Set in Python
1. Set is unique, unordered, collection of  items.
2. Uniques means duplicates are not allowd.
3. unordered means order is not preserved in set, indexing not possible.
4. Mutable : add and remove items, but items inside set are immutable (can not change)
5. Create using curly bracess {}

## Important Funtions in Set
1. set.add(item) : Add items 
2. set.remove(item) : Remove item :  #KeyError : if not found item
3. set.discard(item) : Remove item : remove item if present, if not no error.
4. set1.union(set2) : Combine two sets : combine without duplicates
5. set1.intersection(set2) : Common elements in two sets : return common items
6. set1.difference(set2) : reeturn items  Unique to set1
7. set1.issubset(set2) : Is set1 inside set2
8. set1.issuperset(set2) : Does  set1 contain set2


## Use Cases
1. Removing Duplicates from Data, clean datasets
2. Finding Unique Words in a Text : In Generative AI, when training chatbots, we often need vocabulary.
3. Feature Engineering : In Machine Learning, feature selection is important.
4. Text Preprocessing : Use of Punctuation removal before feading text data to AI model, imp step


## Exercises
1. From a paragraph, find how many unique words are there (ignoring punctuation and case sensitivity).
2. Remove all puncuation and digits in String


[Solutions](sets_exercise.py)