
"""
Problem : person A stand in position x and want to go position y area is of 2,3
Calculate in how many ways person can go to position y
Condition : He only allow to move down or right
"""
"""
def grid_traveler(m,n):
    if (m == 0 or n == 0) :
        return 0
    if (m==1 and n==1):
        return 1
    return grid_traveler(m-1, n) + grid_traveler(m, n-1)

print(grid_traveler(2,3)) #3
print(grid_traveler(4,6)) #56
print(grid_traveler(18,18)) # taking too much time to solve as tree grow very big which take more time to solve from base

"""
"""
print(grid_traveler(18,18)) : taking too much time to solve as tree grow very big which take more time to solve from base
To solve this we will utilise Dynamic programing concept where we
1. will add a memo object 
2. add a base case to return memo value to avoid repeated work 
3. store return value into memo
"""

def grid_traveler(m,n, memo ={}):
    key = m,n  # store as tuple
    if key in memo:
        return memo[key]
    if (m == 0 or n == 0) :
        return 0
    if (m==1 and n==1):
        return 1
    memo[key]= grid_traveler(m-1, n) + grid_traveler(m, n-1)
    return memo[key]

print(grid_traveler(2,3)) # 3
print(grid_traveler(4,6)) # 56
print(grid_traveler(18,18)) # 2333606220

