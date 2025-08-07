from queue import PriorityQueue
queue = PriorityQueue()   #사이즈 제한 시 PriorityQueue(maxsize=10)

queue.put(4)
queue.put(8)
queue.put(6)
queue.put(10)
queue.put(2)

print(queue.qsize())    #q크기 확인
print(queue.get())      #삭제(반환)
print(queue.get()[1])   #역순 삭제은 다 넣고 나서 pop할때만 가능한 사실
"""최대힙 구현하려면 음수 달기"""
print(queue.put(-(10)))
print(-(queue.get())) 
print(queue.empty())    #비었는지 확인
print(queue.full())     #가득찼는지 확인
