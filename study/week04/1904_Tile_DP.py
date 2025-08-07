import sys
input = sys.stdin.readline

N = int(input())

#DP 문제 점화식 찾기..(피보나치와 똑같음)
if N <= 2:
    print(N)
else:
    dp = [0] * (N+1)

    dp[1] = 1
    dp[2] = 2
    #바텀업 방식으로 올라가기
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

    print(dp[N])


"""
if N == 1:
    print(1)

elif N % 2 == 0:
    if N == 2:
        print(2)
    else:
        temp = 2
        temp += (N-1)
        print(temp)
else:
    cnt = 1
    total = 1
    a = N // 2
    for i in range(a):
        total += (N - cnt)
        cnt += 1
    print(total)

"""