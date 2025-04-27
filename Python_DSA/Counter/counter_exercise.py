
from collections import Counter, defaultdict
import re

# Case 1. Counter from a List
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
colors_count=Counter(colors)
print(colors_count) #Counter({'blue': 3, 'red': 2, 'green': 1})

#Case 2. Counter from String
text = 'hello world'
text_count=Counter(text)
print(text_count) #Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

#Case 3. Most Common Elements
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
words_count=Counter(words)
print(words_count) #Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(words_count.most_common(3)) #[('apple', 3), ('banana', 2), ('orange', 1)]

#Case 4. Updating Counter
c=Counter({'apple' : 2, 'grapes' : 1})
c.update(['apple','grapes','banana'])
print(c) #Counter({'apple': 3, 'grapes': 2, 'banana': 1})

""" 
## Example : 
1. AI/NLP — Word Frequency Analysis : When analyzing most frequent words in customer reviews or social media.
2. ML — Class Imbalance Checking :  In datasets, check how many samples per class (important for training fairness!)
3. Gen AI — Token Frequency Preprocessing : Preprocess massive text datasets to build vocabulary frequency tables.
4. Data Science — Error Analysis : After running a model, analyze most frequent misclassification types.
"""

#1. AI/NLP — Word Frequency Analysis : When analyzing most frequent words in customer reviews or social media.
reviews = "great product great value amazing amazing amazing"
word_list=reviews.split()
word_count=Counter(word_list)
print(word_count.most_common()) #[('amazing', 3), ('great', 2), ('product', 1), ('value', 1)]

#2. ML — Class Imbalance Checking :  In datasets, check how many samples per class (important for training fairness!)
labels = [1, 0, 0, 1, 1, 1, 0, 2, 2, 1, 0]
labels_count=Counter(labels)
print(f"Labels Count : {labels_count.most_common()}") #Labels Count : [(1, 5), (0, 4), (2, 2)]

#3. Gen AI — Token Frequency Preprocessing : Preprocess massive text datasets to build vocabulary frequency tables.
tokens = ['the', 'cat', 'sat', 'on', 'the', 'mat', 'the']
token_count=Counter(tokens)
print(token_count) #Counter({'the': 3, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1})

#4. Data Science — Error Analysis : After running a model, analyze most frequent misclassification types.
errors = [('cat', 'dog'), ('cat', 'dog'), ('car', 'truck'), ('car', 'car')]
error_count=Counter([(true, pred) for true, pred in errors if true != pred])
print(error_count)  #Counter({('cat', 'dog'): 2, ('car', 'truck'): 1})

#Exercise 1. Count vowels separately in "beautiful day".
sentence= "beautiful day"
vowels="aeiou"
vowel_counter=Counter()
for char in sentence.lower():
    if char in vowels:
        vowel_counter[char] +=1
# to get all vowel count including zero iterate each vowel, use get() to get each vowel counter, set 0 if not found
final_vowel_count={vowel: vowel_counter.get(vowel,0) for vowel in vowels}
print(final_vowel_count) #{'a': 2, 'e': 1, 'i': 1, 'o': 0, 'u': 2}


#Exercise 2. Given a large list of tweets, find top hashtags
#Idea : When recieve large number of tweets, get most common hasgtags for all tweets
tweets = [
    "Loving the #AI revolution! #MachineLearning",
    "Exploring the depths of #DeepLearning and #AI",
    "Building amazing apps with #Python and #MachineLearning",
    "#Python is versatile! #Coding #Development"
]
hashtags=[]
for tweet in tweets: # iterate through each tweets
    words=tweet.split()
    for word in words: # iterate through each words
        if word.startswith("#"): #if word start with # add that word in hashtags list
            hashtags.append(word)

hashtag_frequency=Counter(hashtags) # count frequency of each hashtags
print(hashtag_frequency)  #Counter({'#AI': 2, '#MachineLearning': 2, '#Python': 2, '#DeepLearning': 1, '
                                    # #Coding': 1, '#Development': 1})


#Exercise 3. 📚 Preprocess a corpus of documents to build a global word frequency dictionary
"""
A corpus is a collection of documents (list of texts).
We want a global vocabulary: how often each word appears in the entire corpus.
Use Counter and re module 
"""
documents = [
    "Machine learning is fun.",
    "Deep Learning and AI are the future!",
    "Python is great for Machine Learning."
]
# import re : as we need it to remove punchuations and spaces
word_document=Counter()

for word in documents:
    #this will remove all punchuations, spaces in word and lower the word
    clean_word=re.sub('r[^a-zA-Z\s]','',word).lower()
    w=word.split() # split each word in list so eachh word count
    word_document.update(w) # update existing counter with new one
print(word_document)

"""
Counter({'Machine': 2, 'is': 2, 'learning': 1, 'fun.': 1, 'Deep': 1, 'Learning': 1, 
         'and': 1, 'AI': 1, 'are': 1, 'the': 1, 'future!': 1, 'Python': 1, 
            'great': 1, 'for': 1, 'Learning.': 1})
"""
