import sys

def n_queen(x):
    global answer
    if x == N:
        answer += 1
        return

    for y in range(N):
        # O(1) 유망성 검사: 현재 열, 두 대각선이 모두 사용 중이 아니어야 함
        if not visited_col[y] and not visited_diag1[x+y] and not visited_diag2[x-y + (N-1)]:
            
            # 1. 선택 (방문 처리)
            visited_col[y] = True
            visited_diag1[x+y] = True
            visited_diag2[x-y + (N-1)] = True
            
            # 2. 다음 단계로 진행
            n_queen(x + 1)
            
            # 3. 선택 취소 (백트래킹)
            visited_col[y] = False
            visited_diag1[x+y] = False
            visited_diag2[x-y + (N-1)] = False


N = int(sys.stdin.readline())
answer = 0

# 방문 기록용 배열들
visited_col = [False] * N           # 열 체크
visited_diag1 = [False] * (2*N - 1) # x+y 대각선 체크
visited_diag2 = [False] * (2*N - 1) # x-y 대각선 체크

n_queen(0)
print(answer)
