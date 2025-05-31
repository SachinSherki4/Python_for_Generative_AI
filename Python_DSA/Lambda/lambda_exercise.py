
#==================== Use Cases ===========================================
#1. Let’s say we have a list of temperatures in Celsius,
# and we want to convert them to Fahrenheit using map()
#Use case: Preprocessing temperature sensor data in AI projects.

temp_celcius= [0, 20, 30, 40]
temp_fehrenheit= list(map(lambda c :(9/5)*c+32, temp_celcius))
print(f"Temprature in Fehrenheit are {temp_fehrenheit}") #[32.0, 68.0, 86.0, 104.0]

#2. Filtering Data : You have a dataset of scores. You want only scores greater than 60.
#Use case: Filtering out low-confidence predictions in a classification model.
scores = [45, 67, 89, 34, 90]
passed= list(filter(lambda s: s >60, scores))
print(f"The score which are greater than 60 are {passed}") #[67, 89, 90]

#3. Sorting Data by Custom Criteria : You have a list of students with marks.
# You want to sort by marks (not name)
#Use case: Sorting models by their accuracy, loss, etc.

students=[("Jack", 31),("Mach",11),("Sid",88),("Harry",1)]
sorted_students= sorted(students, key=lambda x:x[1])
print(f"Sorted List of Students based on Marks are : {sorted_students}") #[('Harry', 1), ('Mach', 11), ('Jack', 31), ('Sid', 88)]

#4. Text Processing :You have a list of sentences and want to convert each to lowercase before feeding to a tokenizer
# Use case: Text normalization before tokenization in LLMs.

sentences = ["Hello World", "GEN AI is Amazing", "python is fun"]
lower_sentance=list(map(lambda s : s.lower(), sentences))
print(f"All sentances converted to Lower Case : {lower_sentance}") #['hello world', 'gen ai is amazing', 'python is fun'

#=============Exercises======================================

#Exercise 1 : Write a lambda function to cube a number.
cub =lambda c : c**3
print(cub(3)) #27

#2. Write a lambda function that returns True if a number is even.
even = lambda n : True if (n%2)!=0 else False
print(even(3)) # True

#3. Convert a list of prices in dollars to rupees (₹1 = $82).
doller_prices = [23,7,5,35,99]
rupees_pricess=list(map(lambda p:p*82,doller_prices))
print(f"list of prices in dollars to rupees : {rupees_pricess}") #[1886, 574, 410, 2870, 8118]

#4. You have a list of words. Use a lambda to filter out words longer than 5 characters.
words= ["Sachin","Ravikant","Matthus", "Marsh","Bob","Anderson"]
filtered_words=list(filter(lambda w :len(w)>5,words))
print(f"words longer than 5 characters : {filtered_words}") #['Sachin', 'Ravikant', 'Matthus', 'Anderson']

#5. Sort a list of tuples based on the second value using lambda
students_marks=[("Jack", 89),("Mach",11),("Sid",88),("Harry",1)]
sorted_tuple=sorted(students_marks, key=lambda m : m[1])
print(f"Sorted Students based on second value : {sorted_tuple}") #[('Harry', 1), ('Mach', 11), ('Sid', 88), ('Jack', 89)]

#6. From a dataset of student scores, create a new list of students who scored above average using lambda.
students_scores=[("harry",78),("Ram",56),("Jack",87),("Bob",61),("Mike",55)]
above_average=list(filter(lambda s:s[1]>60,students_scores))
print(f"new list of students who scored above average of 60 score : {above_average}") #[('harry', 78), ('Jack', 87), ('Bob', 61)]

#7. You have a list of dictionaries. Each dictionary has {"name": str, "accuracy": float}. Sort them by accuracy using lambda.
accuracy=[{"name": "Sachin", "accuracy": 89.99},{"name": "Jack", "accuracy": 90.0},{"name": "Bob", "accuracy": 78.3},{"name": "Mike", "accuracy": 67.7}]
sorted_accuracy=sorted(accuracy, key=lambda a : a['accuracy'])
print(f"Sort them by accuracy : {sorted_accuracy}")
# [{'name': 'Mike', 'accuracy': 67.7}, {'name': 'Bob', 'accuracy': 78.3}, {'name': 'Sachin', 'accuracy': 89.99}, {'name': 'Jack', 'accuracy': 90.0}]

#8. Given a list of full names (e.g., "John Doe"), extract just the first names using map() and a lambda.
full_name=["Jack Mah","Rahul Jaykar","Sachin Tendulkar","Rohit Sharma","Virat Kohli"]
first_names=list(map(lambda n:(n.split(" "))[0],full_name))
#names=list(map(lambda x:x[0], d.split()) for d in full_name)
print(f"First Name list : {first_names}") #['Jack', 'Rahul', 'Sachin', 'Rohit', 'Virat']


#9. You have a list of dictionaries representing students Use map() to extract just the names.
students_data = [
    {"name": "Alice", "score": 80},
    {"name": "Bob", "score": 60},
    {"name": "Charlie", "score": 90}
]
all_name=list(map(lambda x: x['name'], students_data))
print(all_name) #['Alice', 'Bob', 'Charlie']

