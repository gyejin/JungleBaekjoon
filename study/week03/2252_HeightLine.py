import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())    #학생 수(N), 키 비교 횟수(M)

graph = [[] for _ in range(N+1)]    #인접 리스트 그래프
indegree = [0] * (N+1)  #진입차수 받을 리스트

#M개 간선 입력
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)  #단방향 그래프
    indegree[B] += 1    #B에 받으니까 진입차수 +1

def topology_sort():
    result = []     #정렬 결과 담을 배열
    queue = deque() #진입 차수 0인 노드 담을 큐

    #처음 시작할때 진입차수가 0인 노드를 모두 큐에 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
    
    #큐 순회하면서
    while queue:
        now = queue.popleft()   #큐에서 원소 꺼냄
        result.append(now)      #정렬 결과 담음
        
        #해당 원소와 연결된 노드들의 진입 차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            #빼서 진입차수가 0이면 큐에 삽입
            if indegree[i] == 0:
                queue.append(i)

    for j in range(len(result)):
        print(result[j], end=' ')       #print(*result)로 대체 가능

topology_sort()