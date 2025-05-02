import json

with open("json_data.json",'r') as json_file:
    user_data=json.load(json_file)
    for user,age in user_data.items():
        print(f"{user} : {age} ")

"""
Output :
name : Alice 
age : 30 
"""

lis=[[1,3,4],[5,7],[6,8,6,4]]
result=sorted(lis)
print(result)