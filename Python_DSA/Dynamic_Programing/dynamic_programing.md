
### Dynamic Programming
1. DP is a problem solving method used to solve problems with overlapping subproblems and 
2. optimal substructure by breaking down them into smaller subproblems and 
3. solving each once and storing their solutions.

> Two core Techniques
> 1. Top-Down (Memorization) : Recursion + cache
> 2. Bottom-Up (Tabulation) : Iterative Table Filling

### *Memorization - Top Down Approach*
1. Here we are using Dynamic Programing Memorization Technique
2. We first traverse to bottom/base line of tree and then from that start adding and storing key  value in memo with key as root of tree
3. So next time if that root come and first verify whether root present and if present get value 
4. directly from dictionary rather that traversing all to bottom.

> Alvin's Memorization Recipe
> 1. First Make it work
>    1. Visualize the problem as tree
>    2. Implement the tree using recursion
>    3. test it
>  
> 2. Now make it efficient by adding optimize code
>    1. add a default memo object in function where value storing dynamicaly
>    2. now add a base case which will check value already store in memo and return
>    3. store return value into the memo