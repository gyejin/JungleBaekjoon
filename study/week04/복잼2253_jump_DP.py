import sys
import math

input = sys.stdin.readline
N, M = map(int, input().split())

# 작은 돌들의 위치를 빠르게 조회하기 위해 set에 저장
small_stones = set(int(input()) for _ in range(M))

# DP 테이블의 속도 차원의 크기를 계산 (넉넉하게)
# 1+2+...+(x-1) < N  =>  x^2/2 ~ N  => x ~ sqrt(2N)
max_speed = int(math.sqrt(2 * N)) + 2

# dp[돌_번호][속도] = 최소 점프 횟수
# 초기값은 무한대(inf)로 설정
dp = [[float('inf')] * max_speed for _ in range(N + 1)]

# 시작점: 1번 돌에 0번의 점프로, 이전 속도 0으로 와 있다고 가정
dp[1][0] = 0

# 1번 돌부터 N-1번 돌까지 순회
for i in range(1, N):
    # 현재 돌(i)에 도달할 수 없었다면 건너뛴다
    if i in small_stones:
        continue
        
    # 현재 돌(i)에 도달했던 모든 가능한 속도(j)를 확인
    for j in range(max_speed):
        if dp[i][j] == float('inf'):
            continue

        # 가능한 다음 점프 3가지 (속도 j-1, j, j+1)
        for k in [-1, 0, 1]:
            next_speed = j + k
            
            # 속도는 1 이상이어야 함
            if next_speed > 0:
                next_stone = i + next_speed
                
                # 다음 돌이 N번을 넘지 않고, 작은 돌이 아니라면
                if next_stone <= N and next_stone not in small_stones:
                    # DP 테이블 갱신
                    # (기존 값 vs 현재 경로 값) 중 더 작은 값으로
                    dp[next_stone][next_speed] = min(dp[next_stone][next_speed], dp[i][j] + 1)

# N번 돌에 도착한 모든 경우 중, 최소 점프 횟수를 찾는다
result = min(dp[N])

# 만약 result가 여전히 inf라면 도착 불가능, 아니면 result 출력
if result == float('inf'):
    print(-1)
else:
    print(result)

"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    small_stone = int(input())
    dp[small_stone] = -1

print(dp)
dp[1] = 0
dp[2][1] = 1

#for i in range(1, N+1):
"""