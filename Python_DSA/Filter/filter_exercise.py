
""" Use Cases """
""" 1. Data Preprocessing – ML / AI """
#Remove empty or null values from a dataset
# Helps in cleaning datasets before training models.
data = ["data", "", "ML", None, "AI", "",None]
process_data=list(filter(lambda a : a!= "" and a!= None, data)) #['data', 'ML', 'AI']
process_data2= list(filter(lambda a:a, data))
print(process_data) #['data', 'ML', 'AI']
print(process_data2) # ['data', 'ML', 'AI']

"""2. Text Filtering in NLP / Gen AI
     => Filter only long enough prompts for input into GPT:
     =>Used in real-world chatbot and summarization pipelines."""
prompts = ["Hi", "Explain Generative AI", "Ok", "Give summary of chapter 5"]
filtered_prompts=list(filter(lambda a:len(a)>10, prompts))
print(filtered_prompts)  #['Explain Generative AI', 'Give summary of chapter 5']

"""3. Filter Low Probability Tokens (AI Language Models)"""
token_probs = [0.9, 0.2, 0.7, 0.05, 0.85]
token=list(filter(lambda p : p>0.5, token_probs))
print(token)  #[0.9, 0.7, 0.85]

'''Exercises'''
#1. Filter all odd numbers from [1, 2, 3, 4, 5, 6, 7, 8]
number=[1, 2, 3, 4, 5, 6, 7, 8]
odd=list(filter(lambda n : n%2==0, number))
print(f"Odd Numbers are : {odd}") #[2, 4, 6, 8]

#2. From a list of words, filter those that start with the letter "P"
words=["Pratik","Sachin","Rahul","Pravin","Prakash"]
filtered_words=list(filter(lambda w : w.startswith('P'),words))
print(f"Words which are starts with p are : {filtered_words}") #['Pratik', 'Pravin', 'Prakash']

#3. Filter scores above 75 from this list: [60, 90, 88, 45, 77]
scores=[60, 90, 88, 45, 77]
filtered_score=list(filter(lambda s: s>60,scores))
print(filtered_score) #[90, 88, 77]

#4. Filter only students who scored above 70.
students = [{"name": "Anu", "score": 90}, {"name": "Bob", "score": 60}]
filtered_students=list(filter(lambda s : s['score']>70,students))
print(filtered_students)  #[{'name': 'Anu', 'score': 90}]

#5. You are building an AI resume scanner. From a list of candidate dictionaries:
#Filter only those who have "Python" and "Gen AI" in skills.
candidates = [
    {"name": "Ravi", "skills": ["Python", "ML"]},
    {"name": "Meera", "skills": ["Java"]},
    {"name": "Ali", "skills": ["Python", "Gen AI", "Deep Learning"]}
]

filtered_candidates=list(filter(lambda c :("Python" in c['skills'] and "Gen AI" in c['skills']), candidates))
print(filtered_candidates)  #[{'name': 'Ali', 'skills': ['Python', 'Gen AI', 'Deep Learning']}]

#6. Given a list of token probabilities, filter only those between 0.6 and 0.95.
probs = [0.95, 0.43, 0.62, 0.81, 0.99, 0.2]
filtered_prob=list(filter(lambda p : p if p > 0.6 and p <0.95 else None, probs))
print(filtered_prob) #[0.62, 0.81]

#7. You have a dataset of chat prompts. Filter only those that ask a question (end with a ?):
chat_prompts = ["How are you?", "Tell me a joke", "What's AI?", "Thanks"]
filtered_chats=list(filter(lambda c : c.endswith('?'),chat_prompts))
print(filtered_chats) #['How are you?', "What's AI?"]