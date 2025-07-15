import sys
N = int(sys.stdin.readline())
sortNum = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    sortNum[num] += 1

for i in range(1, 10001):
    for j in range(sortNum[i]):
        print(i)