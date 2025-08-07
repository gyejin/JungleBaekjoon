import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]    #그래프 인접 리스트

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)  #도로 정보 단방향

distance = [-1] * (N+1) #최단거리 저장할 리스트, 초기값 -1

def bfs(start):
    queue = deque([start])     #큐에 시작 도시 삽입
    distance[start] = 0      #시작 도시 거리 0(방문 처리)

    while queue:    #큐 요소를 다 돌면서
        now = queue.popleft()   #큐에서 현재 도시 꺼냄
        #현재 도시에서 이동할 수 있는 모든 도시 확인
        for next_node in graph[now]:
            #만약 다음 도시를 아직 방문하지 않았다면
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1     #최단거리를 현재 도시거리 +1
                queue.append(next_node) #다음 도시를 추가
bfs(X)

#최단 거리 K인 도시 찾기 위함
found = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        found = True
if not found:
    print(-1)

