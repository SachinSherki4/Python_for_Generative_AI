from functools import reduce

# Use cases
# creating list, accessing, updating, removing list

fruits = ['apple', 'banana', 'cherry'] # creating
print(fruits[0]) #accessig items in list : apple
fruits[1]="graps"  #modifying list using index
print(fruits)  #['apple', 'Graps', 'cherry']
fruits.append("Peru") # adding  new  items in list
print(fruits) ##['apple', 'Graps', 'cherry', 'Peru']
print(fruits.pop()) # remove and return last items in list : Peru
print(fruits) # ['apple', 'Graps', 'cherry']

for item in fruits: # looping through list using for loop
    print(item)

print(len(fruits)) # 3 len() to get lenth of list
print(sorted(fruits)) # sorted() use to  sort list in alfabetical order ['apple', 'cherry', 'graps']
alfa_num=["sachin",5,1,"sam","jack",7]
#print(sorted(alfa_num)) # TypeError
print(fruits.reverse())

# List momery allocations : here both list_1 and list_2 pointing same memory locations
# so any change in one list will reflect in both list
list_1=[1,2,3]
list_2=list_1
list_1[0]=9
list_2.append(4)
print(list_1,list_2) #[9, 2, 3, 4] [9, 2, 3, 4]

# use cases
#1. Store predictions from ML models
predictions = [0.9, 0.8, 0.75, 0.6]
high_confedence=[x for x in predictions if x > 0.7]
print(high_confedence) #[0.9, 0.8, 0.75]

#2. Data preprocessing : In Machine Learning or Data Science, raw data is stored and manipulated using lists
raw_data = ['  Cat ', 'dOg', 'elephant  ']
clean_data=[x.strip().lower() for x in raw_data]
print(clean_data) #['cat', 'dog', 'elephant']

#3. Handling token lists in GenAI : In Natural Language Processing, lists are used to manage tokens:
sentence = "I love AI"
tokens=sentence.split()
print(tokens) #['I', 'love', 'AI']

#Exercise 1. Remove all odd numbers from this list: [10, 15, 23, 44, 66, 77]
num= [10, 15, 23, 44, 66, 77]
even_num=[x for x in num if x%2 !=0]
print(even_num) #[15, 23, 77]

#Exercise 2. Given a nested list of scores from different models: [[0.8, 0.9], [0.85, 0.7], [0.95, 0.6]],
# extract the maximum score from each inner list.
score=[[0.8, 0.9], [0.85, 0.7], [0.95, 0.6]]
max_score=list(map(lambda x:x[0] if x[0]>x[1] else x[1],score))
print(max_score)  #[0.9, 0.85, 0.95]

#Exercise 3. From a list of sentences, count how many contain the word "AI"
sentences = ["AI is amazing", "ML is subset of AI", "I love coding"]
filtered_sentance=list(sentence for sentence in sentences if "AI" in sentence)
print(filtered_sentance) #['AI is amazing', 'ML is subset of AI']
count_words=sum(1 for sentance in sentences if "AI" in sentance)
print(count_words) #2

#Exercise 4. : Create a list of cubes for numbers from 1 to 10 using list comprehension.
cubes=[x**3 for x in range(1,11)]
print(cubes) #[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

#Exercise 5. Convert a list of words to uppercase using list comprehension.
wordss=["AI is amazing", "ML is subset of AI", "I love coding"]
uppercase=[x.upper() for x in wordss]
print(uppercase) #['AI IS AMAZING', 'ML IS SUBSET OF AI', 'I LOVE CODING']

#Exercise 6. From this list: [10, 25, 36, 47, 58], create a new list with only values divisible by 5.
number=[10, 25, 36, 47, 58]
filtered_num=[x for x in number if x%5==0]
print(filtered_num) #[10, 25]

#Excercise 7. Extract all vowels from a string using list comprehension.
text = "Generative AI is revolutionary"
vowels=['a','e','i','o','u']
filtered_volwels=[v for v in text if v in vowels]
unique_vowels=set(filtered_volwels)
print(filtered_volwels) #['e', 'e', 'a', 'i', 'e', 'i', 'e', 'o', 'u', 'i', 'o', 'a']
print(unique_vowels)

#Exercise 8. Given a list of tuples [(10, 2), (20, 5), (30, 3)], calculate the division of each pair and return a list.
pairs=[(10, 2), (20, 5), (30, 3)]
division=list(reduce(lambda a,b:a/b,x) for x in pairs)
print(division) #[5.0, 4.0, 10.0]


#Exercise 9. Clean and process this messy text list and return only capitalized words with more than 4 letters
data = ['  ml ', ' ai', 'GEN AI ', 'automation', ' code  ']
clean_words=[x.strip() for x in data if x.isupper()]
print(clean_words) #['GEN AI']



# Remove duplicates
seq="Hey! may name is Sachin and my full name is Sachin Sherki"
unique_tokens=[]
unique_tokens=[t for t in seq.split() if t not in unique_tokens]
print(unique_tokens)

