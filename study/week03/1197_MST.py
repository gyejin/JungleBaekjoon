import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())

edges = []  #간선 정보 저장
for _ in range(E):
    A, B, cost = map(int, input().split())  #노드 2개와 비용 저장
    edges.append((cost, A, B))      #리스트에 여러 요소 한꺼번에 튜플로 싸서 넣을 수 있네?

edges.sort()    #간선 비용기준으로 오름차순

#------유니온 파인드-------
parent = list(range(V + 1)) #각 노드의 부모 노드 저장 리스트

#특정 원소가 속한 집합의 최상위 부모(루트)를 찾는 함수
def find_parent(x):
    #자기 자신이 부모가 아니면, 재귀적으로 부모를 찾아서 올라감
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치는 함수
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    #더 작은 번호의 부모로 합침
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

total_cost = 0  #총 가중치
edge_count = 0  #선택된 간선의 수

#정렬된 간선을 하나씩 확인
for cost, a, b in edges:
    #두 노드의 부모가 같지 않다면 (사이클이 아니면)
    if find_parent(a) != find_parent(b):
        #간선을 선택하고 두 집합을 합침
        union_parent(a, b)
        total_cost += cost
        edge_count += 1

        #간선 수가 V-1개면 종료
        if edge_count == V - 1:
            break

print(total_cost)