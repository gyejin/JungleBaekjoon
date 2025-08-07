import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

grid = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

# BFS 함수: 하나의 단지를 탐색하고 그 단지의 집 개수를 반환한다.
def bfs(start_y, start_x):
    # 상,하,좌,우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque([(start_y, start_x)])
    visited[start_y][start_x] = True # 방문 처리
    house_count = 1 # 단지 내 집의 수 (시작점 포함)
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < N and 0 <= nx < N:
                # 길이 있고('1'), 아직 방문하지 않은 집이라면
                if grid[ny][nx] == '1' and not visited[ny][nx]:
                    visited[ny][nx] = True # 방문 처리
                    house_count += 1 # 집 개수 1 증가
                    queue.append((ny, nx))
                    
    return house_count # 탐색이 끝난 단지의 집 개수를 반환

# --- 메인 로직 ---
complex_counts = [] # 각 단지의 집 개수를 저장할 리스트

for i in range(N):
    for j in range(N):
        # 만약 해당 위치가 집('1')이고 아직 방문하지 않았다면 새로운 단지의 시작점
        if grid[i][j] == '1' and not visited[i][j]:
            # bfs를 호출하여 단지를 탐색하고, 반환된 집 개수를 리스트에 추가
            complex_counts.append(bfs(i, j))

# 총 단지 수 출력
print(len(complex_counts))

# 각 단지의 집 개수를 오름차순으로 정렬하여 출력
complex_counts.sort()
for count in complex_counts:
    print(count)