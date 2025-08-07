import sys
from collections import deque

input = sys.stdin.readline
N, M, V = map(int, input().split()) #정점 개수(N), 간선 개수(M), 시작 정점(V)

graph = [[] for _ in range(N+1)]    #그래프 인접 리스트(2차원 배열 N+1 크기)

#M개 간선 정보 받기
for _ in range(M):
    a, b = map(int, input().split())
    #양방향(UnDirected)
    graph[a].append(b)
    graph[b].append(a)

#'정점 번호가 작은 것을 먼저 방문' 리스트 정렬
for i in range(N+1):
    graph[i].sort()

#DFS 깊이 우선 탐색
visited_dfs = [False] * (N+1)   #방문 기록 체크
def dfs(v):
    visited_dfs[v] = True   #현재 노드 방문 처리
    print(v, end=' ')

    #현재 노드와 연결된 다른 노드 재귀적으로 방문
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

#BFS 너비 우선 탐색
visited_bfs = [False] * (N+1)
def bfs(start_v):
    queue = deque([start_v])    #큐 생성
    visited_bfs[start_v] = True #현재 노드 방문 처리

    while queue:    #큐가 다 나올때까지 반복
        v = queue.popleft() #큐에서 하나의 원소를 뽑아 출력
        print(v, end=' ')

        #현재 노드와 연결된 다른 노드 재귀적 방문
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(V)
print()
bfs(V)