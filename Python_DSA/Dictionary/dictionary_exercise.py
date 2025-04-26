import string

mobile_phone = {
    "brand": "Samsung",
    "model": "Galaxy S23",
    "price": 74999,
    "color": "Phantom Black",
    "storage": "256GB",
    "battery": "5000mAh",
    "is_5g": True
}

print(mobile_phone['brand']) #Samsung accessing particular value
print(mobile_phone)
mobile_phone['price']=88888 #Update value
print(mobile_phone)
mobile_phone['update_support']=True # Adding new key-value
print(mobile_phone)
mobile_phone.pop('is_5g') # removing key-value
print(mobile_phone)

student_data = {
    "student_id": 101,
    "name": "Sachin Sherki",
    "age": 24,
    "courses_enrolled": ["AI", "ML", "Data Science"],
    "marks": {
        "AI": 88,
        "ML": 92,
        "Data Science": 85
    },
    "contact_info": {
        "email": "sachin@example.com",
        "phone": "+91-9876543210"
    },
    "is_passed": True
}

print(student_data['marks']['AI']) #88
print(student_data['courses_enrolled'][1]) #ML

# Count frequency of each words
paragraph = "AI is the future. AI will change the world. Machine Learning is a part of AI."

filtered_para=paragraph.translate(str.maketrans('','',string.punctuation))
words=filtered_para.split()

word_count={}
for word in  words:
    word_count[word]=word_count.get(word,0)+1
print(word_count) #{'AI': 3, 'is': 2, 'the': 2, 'future': 1, 'will': 1, 'change': 1, 'world': 1,
                        # 'Machine': 1, 'Learning': 1, 'a': 1, 'part': 1, 'of': 1}