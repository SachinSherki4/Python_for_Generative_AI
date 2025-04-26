import string

"""Sets in Python"""
fruits={"apple","banana","grapes","apple"}
print(fruits)  #{'apple', 'grapes', 'banana'} depulicate remove

number=[2,5,7,7,7,5,9]
number_set=set(number) # set can be create using set() functions, duplicate will be remove
print(number_set) #{9, 2, 5, 7}

## Use Cases
#1. Removing Duplicates from Data, clean datasets
#Use Case : Used heavily in Data Cleaning step before model training.

labels = ["dog", "cat", "dog", "bird", "cat"]
unique_labels=set(labels)
print(unique_labels) #{'bird', 'dog', 'cat'}

#2. Finding Unique Words in a Text : In Generative AI, when training chatbots, we often need vocabulary.
#Use case : Used for creating Vocabulary Lists for Natural Language Processing (NLP).

sentence = "AI is changing the world and AI is powerful"
unique_words=set(sentence.split())
print(unique_words) #{'AI', 'the', 'changing', 'and', 'world', 'powerful', 'is'}

#3. Feature Engineering : In Machine Learning, feature selection is important.
# Suppose we want only unique features across datasets.
#Use Case : Used to merge feature sets intelligently.

features1 = {"height", "weight", "age"}
features2 = {"weight", "age", "salary"}
all_features=features1.union(features2)
print(all_features) #{'weight', 'height', 'salary', 'age'}
#features1.remove("Age") #KeyError
print(features1.intersection(features2)) #{'age', 'weight'} common to both
print(features1.union(features2)) #{'age', 'weight', 'salary', 'height'} combine both
print(features1.difference(features2)) #{'height'} unique to feature1
print(features1.issubset(features2)) #False is feature1 is part of feature2
print(features1.issuperset(features2)) #False is feature2 is part of feature1

#Exercise 1. From a paragraph, find how many unique words are there (ignoring punctuation and case sensitivity).
text = "AI is the future. ai will help everyone."
unique_w=set(w.lower() for w in text.split()) # This will contain punctuations
print(unique_w) # {'help', 'the', 'is', 'future.', 'everyone.', 'will', 'ai'}

filtered_para=text.translate(str.maketrans('','',string.punctuation)) # this code delete all puntucation keeping other unchanged
unique_word=set(w.lower() for w in filtered_para.split())
print(unique_word) #{'help', 'the', 'is', 'future', 'everyone', 'will', 'ai'}

#Exercise 2. Remove all puncuation and digits in String
paragraph = "AI will dominate in 2025!"
remove_items=string.punctuation + "1234567890"
filtered_paragraph=paragraph.translate(str.maketrans('','',remove_items))
print(filtered_paragraph) #AI will dominate in






