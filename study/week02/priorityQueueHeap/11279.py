import sys
from queue import PriorityQueue

input = sys.stdin.readline
N = int(input())
q = PriorityQueue()

for _ in range(N):
    temp = int(input())
    if temp != 0:
        q.put(-temp)    #최대힙 구현을 위한 -음수 붙임
    else:
        if q.empty():
            print(0)
        else:
            print(-(q.get()))   #다시 정상화 시키기 위한 -음수 붙힘