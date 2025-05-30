

#number = [7,[3,4,7]]
def cansum(targetsum,numbers, memo={}):
    if targetsum in memo :
        return memo[targetsum]
    if targetsum == 0 :
        return True
    if targetsum < 0 :
        return False
    for n in numbers:
        reminder = targetsum - n
        if cansum(reminder, numbers, memo) == True:
            memo[targetsum] = True
            return True

    memo[targetsum] = False
    return False

print(cansum(7,[3,4,7]))
print(cansum(7,[2,7]))
print(cansum(7,[2,4,5]))
print(cansum(7,[3,1]))

