
"""
Here we are using Dynamic Programing Memorization Technique
We first traverse to bottom/base line of tree and then from that start adding and storing key  value
in memo with key as root of tree
So next time if that root come and first verify whether root present and if present get value
directly from dictionary rather that traversing all to bottom.

"""
def fibo(n, memo={}):  # here we add memo object which will store root values as key: value
    if n in memo:   # check if key already present (checking to avoid repeated work )
        return memo[n]
    if n <=2:
        return 1
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo) # storing work done in memo as key:value so next time not repeate same calculation
    return memo[n]

print(fibo(7)) #13
print(fibo(8)) #21
print(fibo(13)) #233
print(fibo(50)) #12586269025

