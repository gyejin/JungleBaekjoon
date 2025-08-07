import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

maze = [list(input().strip()) for _ in range(N)]

distance = [[0] * M for _ in range(N)]

def bfs(start_y, start_x):
    #상,하,좌,우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque([(start_y, start_x)])     #큐에 시작 지점 삽입
    distance[start_y][start_x] = 1      #시작 지점 방문 처리

    #큐를 다 순회하면서
    while queue:
        y, x = queue.popleft()
        #상 하 좌 우 찾아보면서
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            #행이 0보다 크고 N보다 작으며, 열이 0보다 크고 M보다 작으면(좌표안에 들어가니까)
            if 0 <= ny < N and 0 <= nx < M:
                #수가 1(지나갈 수 있는 미로칸)이고 and 방문하지 않은 노드면
                if maze[ny][nx] == '1' and distance[ny][nx] == 0:
                    distance[ny][nx] = distance[y][x] + 1   #이전칸에서 거리 +1함
                    queue.append((ny, nx))  #큐에 새로운 위치 추가

bfs(0, 0)

print(distance[N-1][M-1])