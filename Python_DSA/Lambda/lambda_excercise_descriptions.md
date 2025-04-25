## Topic : Lambda Function in Python
1. Def : small, anonymous function (doesn’t have a name)
2. Syntax : lambda arguments: expression
3. Use :1) don’t want to name a function. 
        2) When you want a small, one-line function.
        3) Commonly used with map(), filter(), reduce(), and sorted().
## Use cases
1. Data Preprocessing : we have a list of temperatures in Celsius, and we want to convert them to Fahrenheit using map() 
2. Filtering Data : You have a dataset of scores. You want only scores greater than 60.
3. Sorting Data by Custom Criteria : You have a list of students with marks. You want to sort by marks (not name)
4. Gen AI Use Case – Text Processing : You have a list of sentences and want to convert each to lowercase before feeding to a tokenizer

## Exercise 
1. Write a lambda function to cube a number.
2. Write a lambda function that returns True if a number is even.
3. Convert a list of prices in dollars to rupees (₹1 = $82).
4. You have a list of words. Use a lambda to filter out words longer than 5 characters.
5. Sort a list of tuples based on the second value using lambda.
6. From a dataset of student scores, create a new list of students who scored above average using lambda.
7. You have a list of dictionaries. Each dictionary has {"name": str, "accuracy": float}. Sort them by accuracy using lambda.
8. Given a list of full names (e.g., "John Doe"), extract just the first names using map() and a lambda.

[Solutions](lambda_exercise.py)