from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

queue = deque(range(1, N+1))        #큐 전체 길이 설정

while len(queue) > 1:
    print(queue.popleft(), end=' ') #popleft 가능, 왼쪽에서 빼는거 가능, pop은 () 빈 괄호를 주면 알아서 마지막걸 반환
    queue.append(queue.popleft())   #맨 왼쪽거 뽑아서 뒤에 붙이기

print(queue[0])


"""
from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

# 1부터 N까지의 숫자를 바로 deque로 만든다.
queue = deque(range(1, N + 1))

# 카드가 한 장 남을 때까지 반복
while len(queue) > 1:
    # 1. 맨 위(왼쪽) 카드 버리기
    print(queue.popleft(), end=' ')
    # 2. 그 다음 맨 위(왼쪽) 카드를 뽑아서 맨 뒤(오른쪽)로 옮기기
    queue.append(queue.popleft())

# 마지막에 남은 카드 출력
print(queue[0])
"""