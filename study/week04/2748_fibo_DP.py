import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

memo = [0]*91
def memoization_fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    
    if memo[x] != 0:
        return memo[x]
    
    memo[x] = memoization_fibo(x-1) + memoization_fibo(x-2)
    return memo[x]

dp = [0]*91
def tabulation_fibo(x):
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, x+1):
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[x]

n = int(input())
print(tabulation_fibo(n))
#print(memoization_fibo(n))
