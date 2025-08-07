import sys
input = sys.stdin.readline

N, K = map(int, input().split())    #물건 개수, 배낭 최대 용량 입력
baggage = [[] for _ in range(N)]    #물건 무게, 가치 받을 리스트

for i in range(N):
    W, V = map(int, input().split())    #물건 무게, 가치 입력
    baggage[i].append(W)
    baggage[i].append(V)    #리스트 삽입

dp = [[0] * (K+1) for _ in range(N+1)]  #최대 배낭 가치 계산할 2차원 배열

for i in range(1, N+1):
    weight = baggage[i-1][0]    #가방 무게를 변수에 받음
    value = baggage[i-1][1]     #가방 가치를 변수에 받음
    for j in range(1, K+1):
        if j < weight:  #최대 배낭 용량이 물건 무게보다 작을때
            dp[i][j] = dp[i-1][j]   #이전 배낭 용량 가치 그대로 가져옴
        else:   #최대 배낭 용량이 물건 무게보다 클때
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])   #이전 배낭 용량 가치 vs 현재 배낭 가치 + 현재를 넣고 남은 이전 배낭에서 선택할 수 있느 최선의 가치 

print(dp[N][K])