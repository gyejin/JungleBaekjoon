import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
cnt = 0

for coins in reversed(coin):
    cnt += K // coins
    K = K % coins

print(cnt)

"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())

coin = []
cnt = 0

for _ in range(N):
    C = int(input())
    coin.append(C)

def min_coin(money):
    compare = []
    positive_compare = []
    global cnt
    for i in range(N):
        compare.append(money-coin[i])

    positive_compare = [num for num in compare if num > 0]
    min_pc = min(positive_compare)

    for j in range(len(positive_compare)):
        if positive_compare[j] == min_pc:
            while True:
                money -= coin[j]
                cnt += 1
                if money < 0:
                    money += coin[j]
                    cnt -= 1
                    break
    if money != 0:
        min_coin(money)
    return cnt

print(min_coin(K))
"""