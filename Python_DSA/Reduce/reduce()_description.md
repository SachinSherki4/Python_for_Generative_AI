## Reduce() from functools
1. need to import from functools import reduce
2. reduces a sequence of elements into a single value by applying a function repeatedly.
3. Syntax : reduce(function, iterable)
4. function : function that take two arguments
5. iterable : list, tuple

## AI ML Use Cases
1. Aggregating Model Metrics
  => If you run 5 experiments and get 5 accuracy values, and want the total or average:
2. Text Preprocessing in NLP / Gen AI
  => Join a list of words into a sentence (like what tokenizer outputs)
3. Calculating Losses in ML
  => When training a model on batches, and you want to sum up all batch losses:

   
## Exercise
1. Sum of List Elements
2. Multiplication of all numbers
3. Max value of all
4. Given a list of dictionaries with scores, use reduce() to calculate the total score

[Solutions](reduce_exercise.py)