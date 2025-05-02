import csv
import json

with open("csv_data.csv",newline='') as csv_file:
    data=csv.DictReader(csv_file)
    for row in data:
        print(row['name'],row['age'],row['score'])
"""
Output :
Alice 30 95
Bob 25 88 
"""