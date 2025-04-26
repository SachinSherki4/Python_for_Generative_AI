
## Dictionary in Python
1. Collection that holds key-value pair
2. each key must be unique
3. It is unordered, but from python 3.7 it is ordered.
4. Mutable : can be change, remove, add,
5. Dynamic : can add, remove items anytime

## Use Case in AI ML
1. Dataset row representation : each row in dataset can be store in dictionary.
2. Model Hyperparameter Storage : When training ML models, we store parameters 
3. params = {"learning_rate": 0.01, "epochs": 100, "batch_size": 32}
4. NLP - Word Frequency Count : When cleaning text data, count how many times each word appears
5. word_count = {"AI": 5, "future": 3, "learning": 7}
6. Chatbot Response Mapping : bot_responses = {
    "hi": "Hello! How can I help you?",
    "bye": "Goodbye! Have a nice day!",
}
7. JSON Data Handling : When working with APIs and Big Data, we receive data in JSON (which is basically a dictionary in Python)

## Dictionary Functions
1. d.get(key) : seffer way to access key
2. d.keys() : Return all keys
3. d.values() : Return all values
4. d.items() : Return all key-value pairs
5. d.update(new_data) : Update dictionary
6. d.pop(key) : Remove key and return value

## Counting Frequency of text in AI/ML
1. Text Preprocessing: Counting frequency of words in text data before feeding into ML model.
2. Natural Language Processing (NLP): Building a Word Frequency Table for chatbot, Gen AI model, etc.
3. Sentiment Analysis: How many times "good", "bad", etc. come in customer reviews.
4. Feature Engineering: Creating features based on word counts.


[Solutions](dictionary_exercise.py)