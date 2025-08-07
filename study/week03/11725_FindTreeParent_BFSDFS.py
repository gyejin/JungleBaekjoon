import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs():
    queue = deque([1])  #루트노드 넣고
    parent[1] = -1  #루트는 방문표시로 -1

    #큐가 빌때까지 반복
    while queue:
        #큐에서 현재노드를 꺼내 p에 저장
        p = queue.popleft()
        #현재노드 p의 자식노드를 하나씩 꺼내서
        for c in graph[p]:
            #방문하지 않았으면
            if parent[c] == 0:
                #현재노드가 자식노드c의 부모로 기록
                parent[c] = p
                #자식노드를 큐에 추가하여 다음 탐색 대상
                queue.append(c)
#bfs()

#DFS 깊이우선탐색
def dfs(p_node):
    parent[1] = -1  #루트는 방문 표시로 -1
    #현재 노드와 연결된 모든 자식노드(c_node)확인
    for c_node in graph[p_node]:
        #부모노드가 정해지지 않았다면(방문x)
        if parent[c_node] == 0:
            parent[c_node] = p_node     #현재노드를 자식노드(c_node)의 부모로 기록
            dfs(c_node)     #자식노드를 기준으로 재귀

dfs(1)

for i in range(2, N+1):
    print(parent[i])