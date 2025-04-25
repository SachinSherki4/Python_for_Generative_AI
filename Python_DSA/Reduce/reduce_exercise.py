from functools import reduce

#Use Cases
#==================
#1. Aggregating Model Metrics
# If you run 5 experiments and get 5 accuracy values, and want the total or average
accuracies = [0.8, 0.85, 0.82, 0.78, 0.9]

total=reduce(lambda x,y : x+y, accuracies)
average=total/len(accuracies)+1
print(f"Total : {total} and Average : {average}") #Total : 4.15 and Average : 1.83

#2. Text Preprocessing in NLP / Gen AI
#Join a list of words into a sentence (like what tokenizer outputs)
words = ["AI", "is", "changing", "the", "world"]
sentance=reduce(lambda a,b:a+" "+b,words)
print(sentance) #AI is changing the world

#3. Calculating Losses in ML
# When training a model on batches, and you want to sum up all batch losses:
batch_losses = [0.12, 0.15, 0.18, 0.09]
total_loss = reduce(lambda x, y: x + y, batch_losses)
print(total_loss) #0.54


#Exercise 1. Sum of All Numbers
number1=[2,4,6,67,8]
sum=reduce((lambda x,y : x+y),number1)
print(f"Sum of all numbers is : {sum}") #87

# Exercise 2. Multiplication of all numbers
number2=[2,4,6,67,8]
multi=reduce(lambda x,y : x*y, number2)
print(multi) #25728

#Exercise 3. Maximum Numbers
number3=[2,4,6,67,8]
max=reduce(lambda x,y : (x if x>y else y),number3)
print(max) #67

#Exercise 4. Given a list of dictionaries with scores, use reduce() to calculate the total score
scores = [{"math": 80}, {"math": 90}, {"math": 75}]
total_score=reduce(lambda a,b:(a+b),list(map(lambda x :x['math'],scores)))
print(total_score) #245
# list(map(lambda x :x['math'],scores)) :  this will fetch all score and store in list