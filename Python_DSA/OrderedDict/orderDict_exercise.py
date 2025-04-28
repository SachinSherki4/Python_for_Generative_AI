
from collections import OrderedDict

""" 
## Use Cases
1. AI/ML — Feature Transform Pipeline :Applying scaling, encoding, normalization in correct sequence.
2. GenAI — Vocabulary Building in Tokenizer : When assigning unique IDs to tokens, order matters.
3. Data Science — Metric Tracking for Models : Keep track of metric evaluation during experiments in order.
"""
#1. AI/ML — Feature Transform Pipeline :Applying scaling, encoding, normalization in correct sequence.
pipeline = OrderedDict()
pipeline['scaler'] = 'MinMaxScaler'
pipeline['encoder'] = 'OneHotEncoder'
pipeline['normalizer'] = 'L2Norm'

for step, transformer in pipeline.items():
    print(f"Apply {transformer}")

#2. GenAI — Vocabulary Building in Tokenizer : When assigning unique IDs to tokens, order matters.
tokens = ['the', 'cat', 'sat']
vocab = OrderedDict((token, idx) for idx, token in enumerate(tokens))
print(vocab)
# OrderedDict([('the', 0), ('cat', 1), ('sat', 2)])

#3. Data Science — Metric Tracking for Models : Keep track of metric evaluation during experiments in order.
metrics = OrderedDict()
metrics['accuracy'] = 0.95
metrics['precision'] = 0.92
metrics['recall'] = 0.90

for metric, value in metrics.items():
    print(f"{metric}: {value}")

od = OrderedDict()
od['apple'] = 3
od['banana'] = 2
od['cherry'] = 5
print(od) #OrderedDict({'apple': 3, 'banana': 2, 'cherry': 5})
od.move_to_end('apple')
print(od) #OrderedDict({'banana': 2, 'cherry': 5, 'apple': 3})
print(od.popitem()) #('apple', 3) default Last One
print(od.popitem(last=False)) #('banana', 2) this will remove first one
