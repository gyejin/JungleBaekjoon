#배열 Queue
class ListQueue(object):
    def __init__(self):
        self.queue = []
 
    def dequeue(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)        #이렇게 쓰면 하나 삭제하고 뒤의 모든 요소를 당겨와야함 O(N)이 돼버림, 우린 O(1)을 기대하고 큐를 씀
 
    def enqueue(self, n):
        self.queue.append(n)
        pass
 
    def printQueue(self):
        print(self.queue)

#실행
if __name__ == "__main__":
    lq = ListQueue()
    lq.enqueue(1)
    print(lq.dequeue())

#collections.deque 사용 - 내부적으로 이중 연결 리스트로 구성되어 있음
from collections import deque
dq = deque([])
#실행
dq.append(1)
print(dq.popleft()) # 1

#Queue 모듈 사용
import queue
q = queue.Queue()
#실행
q.put(1)
print(q.get()) # 1

from collections import deque
class Queue(deque):
 
    def enqueue(self, x):
        super().append(x)
 
    def dequeue(self):
        super().popleft()
 
    def display(self):
        for node in self.__iter__():
            print(node)

#연결리스트 Queue, 노드
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
 
 

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
 
    def enqueue(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
 
    def dequeue(self):
        if self.head == None:
            return -1
 
        v = self.head.data
        self.head = self.head.next
 
        if self.head == None:
            self.tail = None
        return v
 
    def print(self):
        curn = self.head
        string = ""
        while curn:
            string += str(curn.data)
            if curn.next:
                string += "->"
            curn = curn.next
        print(string)

#실행
if __name__ == "__main__":
    s = SinglyLinkedList()
    # 원소 추가
    s.enqueue(Node(1))
    print(s.dequeue()) # 1