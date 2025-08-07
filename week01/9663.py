def nqueen(N):
    for q in range(N):
        for w in range(N):
            cmt = 0
            cnt = 0
            r = 0
            c = -1
            c += 1
            if c == N:
                r += 1
                c = 0
            a=[[2]*N for _ in range(N)] #2로 가득 찬 N*N배열


            a[r][c] = 1
            cnt += 1
            for j in range(N):  #행/열 삭제
                a[r][j] = 0
                a[j][c] = 0
            for k in range(1, N):   #대각 삭제
                if (r+k) > N or (c+k) > N:
                    break
                a[r+k][c+k] = 0
            for p in range(N):
                if r == N or c == N:
                    break
                for u in range(N):
                    if a[p][u] == 2:
                        r = p
                        c = u
            

            if N == 8:
                cmt += 1
    return cmt  

N = int(input())
A = nqueen(N)
print(A)

#그 행과 열은 삭제, 대각은 +1, +1씩해서 삭제, 삭제는 0/찍은건 1/남은건 2(기본 2)
#그 다음점을 찍는 것 행기준 최소, 열기준 최소
#재귀 계속 돌다가 더이상 찍을 점이 없을 때(2가 없는 경우) N == 8개이면 cnt += 1
#첫 점을 찍는것 모든 경우

