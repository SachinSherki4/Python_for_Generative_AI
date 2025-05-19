
### Recursion in Python
1. Recursion if functions calling itself.
2. Base Condition in Recusion: Condition where functions stop making recurcise calls.
3. It functions calling itself again and again, you can treat it as sperate call in stack, occupy separate memory.
4. If no Base condtion, function call itself indenite time, memory full - stach overflow error.

### Why recursion
1. To solving biiger and complex problem in a simpler way.
2. You can covert any recursive solution into iteration and wise-versa.
3. It hepl in bearking bigger problems into a smaller problems.

### Visualization of Recursive Tree
``
print(1) -> print(2) -> print(3) -> print(4) -> print(5) -> print(6)
``
### How do decide problem can be sove using recursion
1. CHeck/Identify if you can break program into a smaller problems (fibonacci number). 
2. write recurreance relation - if needed.
3. When you write recursion in formula- Recurrence relation
4. Draw recursion tree - 
   1. See the flow of funtions, how sunctions stoore in stacks, 
   2. Identify and focus on left and right tree calls, how execution flows.
``
fib(n) = fib(n-1) + fib(n-2) // bigger problem break into smaller one
``
3. In fibo -  the based condtion is represent by answers we already have.

## Tail recursion
```commandline

def printn(n):
   if(n>5):
     return
   print(n)
   It is last function - called tail function
   printn(n+1)
```
1. This is last function in call, it dont do anything just handover the flow to printn(n+1) function.
2. It is upto this function to continue further -  it is call tail recursion.


### Types of Recurrance RRelations
1. Linear RR : where tree grow linearly comparing every value in tree - Fibonacci number
``
fib(n) = fib(n-1) + fib(n-2)
``
2. Divide and Conquer : Where program divide the input, compare and remove unwanted input - Binary Search 
```
f(Ns) = O(1) + f(N/2)
O(1) = Write algo with constatnt time complexity (constant time for every comparusion)
f(N/2) = to divide the input 
```



