
## Exercise 1. Given a tuple of numbers (10, 20, 30, 40, 50), print all numbers greater than 25.
num=(10, 20, 30, 40, 50)
t=tuple(x for x in num if x >25)
print(t) #(30, 40, 50)

#Exercise 2. You have a tuple of AI model evaluation results: Find the highest accuracy achieved
results = (0.89, 0.78, 0.92, 0.85, 0.88)
highest_accuracy=max(results)
print(highest_accuracy) #0.92

"""Mini Student Score Project"""
students = [
    ("Sachin", 92),
    ("Amit", 85),
    ("Sneha", 78),
    ("Ravi", 88),
    ("Priya", 95)
]
print("List of Students and their Scores\n===================================")
for student in students:
    print(f"Student Name : {student[0]} and Score : {student[1]}")

print()
print("=======Topper===========")
topper=max(students,key=lambda x :x[1])
student,score=topper
print(f"student Name : {student}, Score : {score}")
print()

print("========Avarage of Student Score=======")
sum_score=sum(score for student,score in students)
average=sum_score/len(students)
print(f"Average : {average}")

"""
List of Students and their Scores
===================================
Student Name : Sachin and Score : 92
Student Name : Amit and Score : 85
Student Name : Sneha and Score : 78
Student Name : Ravi and Score : 88
Student Name : Priya and Score : 95

=======Topper===========
student Name : Priya, Score : 95

========Avarage of Student Score=======
Average : 87.6
"""


