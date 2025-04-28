
from collections import OrderedDict
import pprint

# Step 1: Simulated raw data
data = [
    {'name': 'Alice', 'age': 25, 'salary': None, 'department': 'HR'},
    {'name': 'Bob', 'age': None, 'salary': 50000, 'department': 'Engineering'},
    {'name': 'Charlie', 'age': 35, 'salary': 60000, 'department': None},
    {'name': 'David', 'age': 45, 'salary': 70000, 'department': 'Engineering'}
]

# Step 2: Define preprocessing steps in correct order using OrderedDict
pipeline=OrderedDict()

# Handle missing values
def filling_missing_values(data):
    for entry in data:
        if entry['age'] is None:
            entry['age']=30 # default ege
        if entry['salary'] is None:
            entry['salary']=50000 #default salary
        if entry['department'] is None:
            entry['department']="Unknown" # default department
    return  data # return updated data

# Feature Scalling : Normallising Salary between 0 and 1
def scale_salary(data):
    salaries=[entry['salary'] for entry in data] # storing all salaries in list
    min_salary=min(salaries) # minimum salary
    max_salary=max(salaries) # maximum salary
    # now add salary_scaled by calculating salary scale
    for entry in data:
        entry['salary_scaled']=(entry['salary']-min_salary)/(max_salary-min_salary)
    return  data  # return updated data

# Encoding departement
def encode_department(data):
    department_mapping={'HR': 1, 'Engineering': 2, 'Unknown': 0}
    # add department encoding, assign department mapping for known and 0 for unknown
    for entry in data:
        entry['department_encoded']=department_mapping.get(entry['department'],0)
    return  data

# Create new feature: Age group
def create_age_group(data):
    for entry in data:
        if entry['age'] <30 :
            entry['age_group']='young'
        elif entry['age']<40 :
            entry['age_group'] ='mid'
        else:
            entry['age_group']='Senior'
    return data

# Step 3: Add all functions to the pipeline
pipeline["Fill Missing Values"] = filling_missing_values
pipeline["Scale Salary"]=scale_salary
pipeline["Encode Department"]=encode_department
pipeline["Create Age Group"]=create_age_group

# Step 4: Apply transformations in order
processed_data=data  # to get updated data after every transformation
for step_name, step_function in pipeline.items():
    print(f"Applying Step : {step_name}")
    processed_data=step_function(processed_data)

#Final Output
print("\n✅ Processed Data:")
pprint.pprint(processed_data)

"""
✅ OrderedDict ensures your machine learning data is prepared exactly as needed!

Applying Step : Fill Missing Values
Applying Step : Scale Salary
Applying Step : Encode Department
Applying Step : Create Age Group

✅ Processed Data:
[{'age': 25,
  'age_group': 'young',
  'department': 'HR',
  'department_encoded': 1,
  'name': 'Alice',
  'salary': 50000,
  'salary_scaled': 0.0},
 {'age': 30,
  'age_group': 'mid',
  'department': 'Engineering',
  'department_encoded': 2,
  'name': 'Bob',
  'salary': 50000,
  'salary_scaled': 0.0},
 {'age': 35,
  'age_group': 'mid',
  'department': 'Unknown',
  'department_encoded': 0,
  'name': 'Charlie',
  'salary': 60000,
  'salary_scaled': 0.5},
 {'age': 45,
  'age_group': 'Senior',
  'department': 'Engineering',
  'department_encoded': 2,
  'name': 'David',
  'salary': 70000,
  'salary_scaled': 1.0}]
"""