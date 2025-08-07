import sys

def dfs(depth):
    global max_sum
    
    # 종료 조건: N개의 숫자를 모두 골라 순열을 완성했을 때
    if depth == N:
        current_sum = 0
        for i in range(N - 1):
            current_sum += abs(temp[i] - temp[i+1])
        
        # 최댓값 갱신
        if current_sum > max_sum:
            max_sum = current_sum
        return

    # 재귀 호출: 모든 숫자를 확인하며
    for i in range(N):
        # 아직 방문(사용)하지 않은 숫자라면
        if not visited[i]:
            # 1. 선택
            visited[i] = True  # 사용했다고 체크
            temp.append(numbers[i]) # 현재 순열에 추가
            
            # 2. 다음 단계로 진행
            dfs(depth + 1)
            
            # 3. 선택 취소 (백트래킹)
            temp.pop() # 순열에서 다시 빼기
            visited[i] = False # 미사용 상태로 되돌리기

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

max_sum = 0
visited = [False] * N # 방문 체크리스트
temp = [] # 현재 만들어지고 있는 순열을 담을 리스트

dfs(0) # 0개의 숫자를 뽑은 상태에서 시작
print(max_sum)
