import sys

def n_queen(x):
    global answer
    # x가 N과 같아지면, 마지막 행까지 퀸을 다 놓았다는 뜻 -> 경우의 수 1 증가
    if x == N:
        answer += 1
        return

    # 현재 x행의 모든 열(0부터 N-1)에 퀸을 놓아본다.
    for y in range(N):
        board[x] = y # (x, y)에 퀸을 놓는다.
        
        # 유망한지(안전한지) 확인
        is_promising = True
        # 이전 행들을 확인
        for i in range(x):
            # 같은 열이거나, 대각선에 있으면 유망하지 않음
            if board[i] == board[x] or abs(board[i] - board[x]) == abs(i - x):
                is_promising = False
                break
        
        # 유망하다면, 다음 행으로 진행 (재귀 호출)
        if is_promising:
            n_queen(x + 1)


N = int(sys.stdin.readline())
# board[x] = y 는 x행 y열에 퀸이 놓였다는 의미. 1차원 리스트로 충분.
board = [0] * N
answer = 0

n_queen(0) # 0번 행부터 시작
print(answer)
