import sys
from collections import deque   #que 생성 라이브러리

input = sys.stdin.readline
N = int(input())

queue = deque(range(1, N+1))        #que 길이 적정

while len(queue) > 1:   #que에 카드수가 1이하면 종료
    queue.popleft()     #맨 왼쪽꺼 뺌(홀수 인덱스)
    queue.append(queue.popleft())   #맨 왼쪽꺼 뺌(짝수 인덱스)

print(queue[0])
#que는 항상 O(1) 시간복잡도를 가진다.