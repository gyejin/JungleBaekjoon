N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

rain = 0
List = []

visted = [[0]*N for _ in range(N)]  #0은 기본, 1은 안잠긴데, 2는 연속된곳

for i in range(1, 101):
    result = 0
    if (max(map(max, arr))) < i:
        break
    else:
        rain += 1
        for j in range(N):
            for k in range(N):
                if arr[j][k] > rain:
                    visted[j][k] = 1

        for p in range(N):
            if (p+1) >= N:
                break
            for o in range(N):
                if (o+1) >= N:
                    break
                else:
                    cnt = 0
                    if visted[p][o] == 1:
                        visted[p][o] = 2
                        if visted[p+1][o] == 1:
                            visted[p+1][o] = 2
                            cnt += 1
                        if visted[p][o+1] == 1:
                            visted[p][o+1] = 2
                            cnt += 1
                        if visted[p-1][o] == 1:
                            visted[p-1][o] = 2
                            cnt += 1
                        if visted[p][o-1] == 1:
                            visted[p][o-1] = 2
                            cnt += 1
                        if cnt > 0:
                            result += 1
                    temp = 0
                    if visted[p][o] == 2:
                        if visted[p+1][o] == 1:
                            visted[p+1][o] = 2
                        else:
                            temp += 1
                        if visted[p][o+1] == 1:
                            visted[p][o+1] = 2
                        else:
                            temp += 1
                        if visted[p-1][o] == 1:
                            visted[p-1][o] = 2
                        else:
                            temp += 1
                        if visted[p][o-1] == 1:
                            visted[p][o-1] = 2
                        else:
                            temp += 1
                        if temp == 4:
                            result += 1
                        
        List.append(result)

print(max(List))

"""
import sys
# 재귀가 깊어질 수 있으므로, 재귀 깊이 제한을 넉넉하게 풀어줌
sys.setrecursionlimit(10000)

# DFS 함수: (x, y) 지점과 연결된 모든 안전 영역을 방문 처리
def dfs(x, y, rain_height, visited, arr, N):
    # 1. 범위를 벗어나는지 확인
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    
    # 2. 이미 방문했거나 물에 잠겼는지 확인
    if visited[x][y] or arr[x][y] <= rain_height:
        return
        
    # 3. 위 조건들을 통과했다면, 현재 위치를 방문 처리
    visited[x][y] = True
    
    # 4. 상하좌우 인접한 곳으로 다시 DFS 진행
    dfs(x - 1, y, rain_height, visited, arr, N) # 상
    dfs(x + 1, y, rain_height, visited, arr, N) # 하
    dfs(x, y - 1, rain_height, visited, arr, N) # 좌
    dfs(x, y + 1, rain_height, visited, arr, N) # 우

# --- 메인 로직 시작 ---

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 최대 높이를 구해서 반복 범위를 최적화
# 아무 지역도 물에 잠기지 않는 경우도 있으므로, 최소 1개의 안전영역은 보장됨
max_safe_zones = 1 
max_height = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > max_height:
            max_height = arr[i][j]

# 1. 비의 높이를 1부터 최대 높이까지 바꿔가며 반복 (JO의 원래 아이디어)
for h in range(1, max_height + 1):
    # 2. 각 높이마다 방문 기록용 visited 리스트와 안전 영역 개수 초기화
    visited = [[False] * N for _ in range(N)]
    current_safe_zones = 0
    
    for i in range(N):
        for j in range(N):
            # 3. 새로운 안전 영역 덩어리를 발견하면 DFS 시작 및 개수 +1 (가장 핵심적인 수정 부분)
            # 현재 위치가 물에 잠기지 않았고, 아직 방문하지 않았다면
            if arr[i][j] > h and not visited[i][j]:
                current_safe_zones += 1
                dfs(i, j, h, visited, arr, N) # DFS로 연결된 모든 곳을 방문 처리
                
    # 4. 현재 높이에서의 안전 영역 개수와 전체 최댓값 비교 후 갱신
    if current_safe_zones > max_safe_zones:
        max_safe_zones = current_safe_zones

print(max_safe_zones)
"""
