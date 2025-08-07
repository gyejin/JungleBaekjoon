import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

visited = [False] * (N+1)

#간선 정보 받기
for _ in range(M):
    u, v = map(int, input().split())
    #양방향 그래프
    graph[u].append(v)
    graph[v].append(u)

#깊이 우선 탐색 DFS
def dfs(v):
    visited[v] = True   #방문 체크
    for i in graph[v]:
        if not visited[i]:  #방문 안한거면 재귀
            dfs(i)

count = 0

for j in range(1, N+1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)