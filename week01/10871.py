N, X = map(int, input().split())
num = list(map(int, input().split()))

#틀림num.append(int(input().split()))

for i in range(0, N):
    if num[i] < X:
        print(num[i], end=' ')
    
