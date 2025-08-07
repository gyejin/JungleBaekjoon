A = int(input())
B = int(input())
C = int(input())

D = str(A * B * C)

for i in range(0, 10):
    cnt = 0
    for j in range(len(D)):
        if i == int(D[j]):
            cnt += 1
    print(cnt)
