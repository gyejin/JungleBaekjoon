import sys

def recursion_binary_search(data, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return recursion_binary_search(data, target, start, mid - 1)
    else:
        return recursion_binary_search(data, target, mid + 1, end)

input = sys.stdin.readline
N = int(input())
getCard = list(map(int, input().split()))
getCard.sort()  #sort 빠뜨리지 말기

M = int(input())
searchCard = list(map(int, input().split()))

for j in range(M):
    correct = recursion_binary_search(getCard, searchCard[j], 0, N-1)
    if correct == None:
        print(0, end=' ')
    else:
        print(1, end=' ')
    