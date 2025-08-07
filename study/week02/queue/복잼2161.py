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