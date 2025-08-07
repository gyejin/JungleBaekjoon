import sys

input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

# 하얀색(0)과 파란색(1) 종이의 개수를 저장할 변수 초기화
white_count = 0
blue_count = 0

#(x, y)를 시작점으로 하는 n x n 크기의 정사각형을 검사하는 함수
def solve(x, y, n):
    global white_count, blue_count
    
    # 현재 확인하는 정사각형의 첫 번째 칸의 색깔을 기준으로 삼는다.
    color = paper[y][x]
    
    # 현재 정사각형 내의 모든 칸을 확인
    for i in range(y, y + n):
        for j in range(x, x + n):
            # 기준 색(color)과 다른 색이 하나라도 발견되면,
            if paper[i][j] != color:
                # 더 이상 확인할 필요 없이 바로 4등분하여 재귀 호출
                half = n // 2
                solve(x, y, half)            # 1사분면 (왼쪽 위)
                solve(x + half, y, half)     # 2사분면 (오른쪽 위)
                solve(x, y + half, half)     # 3사분면 (왼쪽 아래)
                solve(x + half, y + half, half)  # 4사분면 (오른쪽 아래)
                return  # 분할했으므로 현재 함수는 종료
    
    # 위 반복문이 break 없이 모두 통과했다면, 모든 칸의 색이 같다는 의미
    if color == 0:
        white_count += 1
    else:
        blue_count += 1

# 전체 종이(0, 0)에서 시작하는 N x N 크기로 첫 탐색 시작
solve(0, 0, N)

# 결과 출력
print(white_count)
print(blue_count)

"""
def color_paper_count(x, y, N):
    global white_cnt, blue_cnt, temp
    temp = 0
    color = arr[y][x]
    for i in range(x):
        for j in range(y):
            if arr[x][y] != color:
                break
            elif arr[x][y] == color:
                temp += 1
                continue
        if temp == ((N*N) / 4):
            if color == 0:
                white_count += 1
            elif color == 1:
                blue_count += 1
        return
    
    new_N = N //2
    color_paper_count(x,y,new_N)
"""
"""
import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
Ncnt = 0

def color_paper(arr, N):
    if len(arr) <= 1:
        return 
    mid = N // 2
    left_up = arr[:mid][:mid]
    right_up = arr[mid:][:mid]
    left_down = arr[:mid][mid:]
    right_down = arr[mid:][mid:]
    return check_color(left_up, right_down, left_down, right_down, mid)
    
def check_color(left_up, right_up, left_down, right_down, m):
    global cnt, Ncnt
    if left_up.count(1) != m*m:
        color_paper(left_up, m)
    elif left_up.count(0) == N*N:
        Ncnt += 1
    if right_up.count(1) != m*m:
        color_paper(left_up, m)
    elif right_up.count(0) == m*m:
        Ncnt += 1
    if left_down.count(1) != m*m:
        color_paper(left_up, m)
    elif left_down.count(0) == m*m:
        Ncnt += 1
    if right_down.count(1) != m*m:
        color_paper(left_up, m)
    elif right_down.count(0) == m*m:
        Ncnt += 1
    cnt += 1

color_paper(arr, N)
print(cnt)
print(Ncnt)
"""