import sys
# 재귀 깊이 제한을 풀어줘야 함 (N이 크면 RecursionError 발생 가능)
sys.setrecursionlimit(100000)

# DFS 함수 정의
def dfs(x, y, rain_height):
    # 범위를 벗어나거나, 이미 방문했거나, 물에 잠겼으면 종료
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if visited[x][y] or arr[x][y] <= rain_height:
        return False
    
    # 현재 노드 방문 처리
    visited[x][y] = True
    
    # 상, 하, 좌, 우 재귀적으로 호출
    dfs(x - 1, y, rain_height)
    dfs(x + 1, y, rain_height)
    dfs(x, y - 1, rain_height)
    dfs(x, y + 1, rain_height)
    return True

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_safe_zones = 0

# 0 (비가 안 올 때) 부터 최대 높이까지 모든 강수량 확인
max_height = max(map(max, arr))
for h in range(max_height + 1):
    visited = [[False] * N for _ in range(N)]
    current_safe_zones = 0
    
    for i in range(N):
        for j in range(N):
            # 현재 위치가 안전하고, 아직 방문 안 했다면
            if arr[i][j] > h and not visited[i][j]:
                # 새로운 안전 영역 발견!
                dfs(i, j, h) # DFS로 연결된 모든 곳을 방문 처리
                current_safe_zones += 1
    
    # 최댓값 갱신
    if current_safe_zones > max_safe_zones:
        max_safe_zones = current_safe_zones

# 비가 아무리 많이 와도 잠기지 않는 땅이 없을 경우, 안전영역은 1개(아무것도 없는 상태)가 될 수 있음
# 하지만 문제 조건상 높이는 1 이상이므로, 비가 오지 않는 경우(h=0)는 항상 안전영역이 최소 1개 이상임.
# 만약 max_safe_zones가 0이면(모든 땅의 높이가 0인 극단적 케이스), 1을 출력해야 함.
# 하지만 이 문제에서는 그럴 일이 없으므로 그냥 출력.
print(max_safe_zones)
