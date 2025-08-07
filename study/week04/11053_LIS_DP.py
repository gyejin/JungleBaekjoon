import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))

dp = [1] * N    #자기자신이면 무조건 1

for i in range(1, N):   #첫번째부터 앞이랑 하나씩 비교
    for j in range(i):  # ""
        if numList[j] < numList[i]:     #앞에꺼랑 비교해서 더 크면
            dp[i] = max(dp[i], dp[j] + 1)       #기존의 길이에서 +1 한거나 같은 수가 있을 수 있으므로 기존거랑 비교해서 가장 큰거 저장

print(max(dp))  #길이가 가장 긴거 출력

"""
dp = [0] * (N)
cnt = 0

if N == 1:
    print(0)
    exit()
else:
    for i in range(N):
        if i == 0:
            num = numList[i]
            dp[i] = num
            continue
        else:
            if num <= max(dp):
                continue
            dp[i] = num

print(dp)
for j in range(N):
    if dp[j] == 0:
        continue
    else:
        cnt +=1 

print(cnt)
"""