import string

# Concatenation
a = "AI"
b = "is amazing"
print(a + " " + b)  # AI is amazing

# Length
print(len("Machine Learning"))  # 16

# Repetition
print("AI " * 2)  # AI AI

# Membership
print("future" in "AI is the future")  # True

# Accessing
text = "Python"
print(text[2])  # 't'

words = ['AI', 'ML', 'Data']
joining_words=' '.join(words)
print(joining_words) #AI ML Data

name = "Sachin"
age = 25
print("My name is {0} and age is {1}".format(name, age)) #My name is Sachin and age is 25
print(f"My name is {name} and age is {age}")

#Exercise 1. Replace all spaces ' ' with '-' in a given sentence
sentence= "AI is the future of technology"
w=sentence.replace(' ','-')
print(w) #AI-is-the-future-of-technology

#Exercise 2. Find the index of the word "future" in "AI is the future of technology"
for index, word in enumerate(sentence.split()):
    if word =="future":
        print(f"{word} : {index}") #future : 3

#Exercise 3. From a paragraph, find and print the top 3 most repeated words.

paragraph=("AI is changing the world. AI is making life easier. "
           "Many industries are adopting AI to solve complex problems. "
           "Machine learning and AI together are building smart solutions. "
           "AI, AI, and more AI — everywhere you see, AI is creating new opportunities")

filtered_para= paragraph.translate(str.maketrans('','',string.punctuation)) # remove all punctuations
words_counts={}
for word in filtered_para.split():
    words_counts[word]=words_counts.get(word,0)+1 # this will count accurance of each words
#print(words_counts)
sorted_words=sorted(words_counts.items(),key=lambda x:x[1], reverse=True) # this will reverse based on accurance
for words,index in sorted_words[:3]: #this will fetch only first three values
    print(f"{words} : {index}")
"""
AI : 8
is : 3
are : 2 """

#Exercise 4. Write a function that takes a sentence and returns the words in reverse order
sent="AI is booming"
revers=' '.join(sent.split()[::-1])
print(revers) #booming is AI



