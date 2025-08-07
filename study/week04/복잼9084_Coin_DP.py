import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    
    dp = [0] * (M+1)
    dp[0] = 1   #초깃값 설정이 젤 중요

    for coin in coins:
        for j in range(coin, M+1):
            dp[j] = dp[j] + dp[j - coin]    #dp[2]는 dp[0]에 2원 더한거 => dp[j] = dp[j-coin], 1 or 2원 둘다 쓰면 dp[j] = dp[j] + dp[j-coin]
    
    print(dp)
    print(dp[M])