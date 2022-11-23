profits = [1,2,5,6]
wt = [2,3,4,5]
C = 8
n = len(profits)

t = [[-1 for i in range(C+1)] for j in range(n+1)]

def knapsack(wt, profits, C, n):
    if n==0 or C==0:
        return 0;
    
    if t[n][C] != -1:
        return t[n][C]
    
    if wt[n-1]<=C:
        t[n][C] = max(profits[n-1] + knapsack(wt, profits, C - wt[n-1], n-1),
        knapsack(wt, profits, C, n-1))
        return t[n][C]
    elif wt[n-1]>C:
        t[n][C] = knapsack(wt, profits, C, n-1)
        return t[n][C]

print(knapsack(wt, profits, C, n))
