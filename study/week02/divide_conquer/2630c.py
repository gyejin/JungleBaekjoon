import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white_cnt = 0
blue_cnt = 0

def color_paper(x, y, n):
    global white_cnt, blue_cnt
    color = arr[y][x]

    for i in range(y, y+n):
        for j in range(x, x+n):
            if arr[i][j] != color:
                half = n // 2
                color_paper(x, y, half)
                color_paper(x+half, y, half)
                color_paper(x, y+half, half)
                color_paper(x+half, y+half, half)
                return
                
    if color == 0:
        white_cnt += 1
    else:
        blue_cnt += 1

color_paper(0, 0, N)

print(white_cnt)
print(blue_cnt)