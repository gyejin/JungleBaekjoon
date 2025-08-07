class Node:
    def __init__(self, data):
        self.data = data  # 노드가 저장할 데이터
        self.next = None  # 다음 노드를 가리키는 포인터

class CircularLinkedList:
    def __init__(self):
        self.head = None  # 리스트의 시작을 가리키는 포인터

    def insert_front(self, data):
        """리스트의 맨 앞에 새로운 노드를 삽입합니다."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    def insert_end(self, data):
        """리스트의 맨 끝에 새로운 노드를 삽입합니다."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def delete_node(self, key):
        """리스트에서 주어진 값을 가진 첫 번째 노드를 삭제합니다."""
        if self.head is None:
            return
        
        temp = self.head
        prev = None

        # 리스트에 노드가 하나인 경우
        if temp.data == key and temp.next == self.head:
            self.head = None
            return

        # 리스트의 첫 번째 노드를 삭제하는 경우
        if temp.data == key:
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            return

        # 리스트의 중간 또는 마지막 노드를 삭제하는 경우
        while temp.next != self.head:
            prev = temp
            temp = temp.next
            if temp.data == key:
                prev.next = temp.next
                return

    def search(self, key):
        """리스트에서 주어진 값을 가진 노드를 찾습니다."""
        if self.head is None:
            return False
        
        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def traverse(self):
        """리스트의 모든 노드를 순서대로 방문합니다."""
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("HEAD")

# 사용 예시
cll = CircularLinkedList()
cll.insert_front(1)
cll.insert_front(2)
cll.insert_end(3)
cll.traverse()  # Output: 2 -> 1 -> 3 -> HEAD
cll.delete_node(1)
cll.traverse()  # Output: 2 -> 3 -> HEAD
print(cll.search(2))  # Output: True
print(cll.search(4))  # Output: False