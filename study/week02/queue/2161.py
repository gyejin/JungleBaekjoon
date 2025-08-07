import sys
input = sys.stdin.readline

N = int(input())
card = []

for i in range(1, N+1):
    card.append(i)

card.reverse()

while len(card) != 1:
    print(card.pop(), end=' ')
    temp = card.pop()
    card.insert(0, temp)        #insert는 O(N) 시간이 많이걸림!! 이건 왼쪽에서 숫자를 빼야하니까 que를 사용해보자!
print(card[0])