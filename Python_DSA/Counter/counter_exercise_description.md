
## Counter class in Python Collections Module

1. Counter is class in Collections module help to count frequency of hashable objects(list,string, tuple, dict, etc)
2. from collections import Counter
3. Syntax : c=Counter(iterable_or_mapping)

## Use Cases
1. Counter from a List
2. Counter from a string
3. Most Common Elements
4. Updating Counter

## Why is Counter useful? : In real-world AI/ML/GenAI projects, you often have to analyze frequencies
1. Words in text data
2. Labels in datasets
3. Tokens in language models
4. Items bought by users
5. Error types in model outputs
6. Sentiment classes

## Example : 
1. AI/NLP — Word Frequency Analysis : When analyzing most frequent words in customer reviews or social media.
2. ML — Class Imbalance Checking :  In datasets, check how many samples per class (important for training fairness!)
3. Gen AI — Token Frequency Preprocessing : Preprocess massive text datasets to build vocabulary frequency tables.
4. Data Science — Error Analysis : After running a model, analyze most frequent misclassification types.

## Exercises 
1. Count vowels separately in "beautiful day".
2. Given a large list of tweets, find top hashtags
    => #Idea : When recieve large number of tweets, get most common hasgtags for all tweets
3. 📚 Preprocess a corpus of documents to build a global word frequency dictionary


[Solutions](counter_exercise.py)