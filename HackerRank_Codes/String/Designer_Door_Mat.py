

"""

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

"""


n,m= map(int,input().split())
pattern=[]

for i in range(1, n,2): # this will take odd number time
    s= (".|."*i).center(m,"_")
    pattern.append(s)
pattern.append("WELCOME".center(m,"_"))
for i in range(n-2,0,-2):
    s = (".|." * i).center(m, "_")
    pattern.append(s)

for i in pattern:
    print(i)