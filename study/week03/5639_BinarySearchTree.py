import sys

sys.setrecursionlimit(10**6)    #재귀호출횟수 제한 (노드 개수 10,000개)

input = sys.stdin.readline
preorder_list = []  #전위 순회 결과 저장 리스트

#EOF(개행)이 나올때까지 숫자 계속 입력
while True:
    try:
        preorder_list.append(int(input()))
    except:
        break

#후위 순회 수행하고 출력하는 재귀 함수
#start, end는 현재 탐색하고 있는 서브트리의 preorder_list상의 인덱스 범위
def postorder(start, end):
    #재귀 종료조건 : start가 end보다 커지면 해당 서브트리는 없는 것
    if start > end: 
        return
    #순회 결과 첫번째 요소가 서브트리 루트
    root = preorder_list[start]

    #오른쪽 서브트리 시작 인덱스, 기본값은 오른쪽 서브트리가 없는 경우 end+1
    mid = end+1

    #루트 다음부터 끝까지 탐색하여 루트보다 큰 첫 값을 찾음, 그게 오른쪽 서브트리 시작지점
    for i in range(start + 1, end + 1):
        if preorder_list[i] > root:
            mid = i
            break
    #왼쪽 서브트리 재귀(루트 다음부터 오른쪽 시작 전까지)
    postorder(start+1, mid-1)

    #오른쪽 서브트리 재귀(오른쪽 시작점부터 끝까지)
    postorder(mid, end)

    print(root)

postorder(0, len(preorder_list) - 1)