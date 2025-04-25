## Filter Function
1. used to filter out items from a list (or any iterable) based on a condition.
2. It returns only those items that make the condition True.
3. Syntax : filter(function, iterable)
4. It returns a filter object, which we usually convert to a list or tuple.

## Use Cases
1. Data Preprocessing – ML / AI
   => Remove empty or null values from a dataset
   => Helps in cleaning datasets before training models.
2. Text Filtering in NLP / Gen AI
   => Filter only long enough prompts for input into GPT
   => Used in real-world chatbot and summarization pipelines.
3. Filter Low Probability Tokens (AI Language Models)
   => Useful in sampling strategies like Top-K, Top-P in LLMs.


## Exercises
1. Filter all odd numbers from [1, 2, 3, 4, 5, 6, 7, 8]
2. From a list of words, filter those that start with the letter "P"
3. Filter scores above 75 from this list: [60, 90, 88, 45, 77]
4. Filter only students who scored above 70. students = [{"name": "Anu", "score": 90}, {"name": "Bob", "score": 60}]
5. You are building an AI resume scanner. From a list of candidate dictionaries:
   => Filter only those who have "Python" and "Gen AI" in skills.
6. Given a list of token probabilities, filter only those between 0.6 and 0.95.
7. You have a dataset of chat prompts. Filter only those that ask a question (end with a ?):


[Solutions](filter_exercise.py)


