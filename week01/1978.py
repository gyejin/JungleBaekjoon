N = int(input())
num = list(map(int, input().split()))
sosu = 0

for i in range(len(num)):
    cnt = 0
    for j in range(1, (num[i]+1)):
        if cnt <= 2:
            if num[i] % j == 0:
                cnt += 1
        else:
            break
    if cnt == 2:
        sosu += 1

print(sosu)
