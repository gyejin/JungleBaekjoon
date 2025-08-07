class DoublyNode:
    def __init__(self, data):
        self.data = data  # 노드가 저장할 데이터
        self.prev = None  # 이전 노드를 가리키는 포인터
        self.next = None  # 다음 노드를 가리키는 포인터

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # 리스트의 시작을 가리키는 포인터

    def insert_front(self, data):
        """리스트의 맨 앞에 새로운 노드를 삽입합니다."""
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_end(self, data):
        """리스트의 맨 끝에 새로운 노드를 삽입합니다."""
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_node(self, node):
        """주어진 노드를 삭제합니다."""
        if self.head is None or node is None:
            return

        if self.head == node:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

        node = None

    def search(self, key):
        """리스트에서 주어진 값을 가진 노드를 찾습니다."""
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def traverse_forward(self):
        """리스트의 모든 노드를 순서대로 방문합니다 (정방향)."""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        """리스트의 모든 노드를 순서대로 방문합니다 (역방향)."""
        current = self.head
        last = None
        while current:
            last = current
            current = current.next

        while last:
            print(last.data, end=" <-> ")
            last = last.prev
        print("None")

# 사용 예시
dll = DoublyLinkedList()
dll.insert_front(1)
dll.insert_front(2)
dll.insert_end(3)
dll.traverse_forward()  # Output: 2 <-> 1 <-> 3 <-> None
dll.traverse_backward() # Output: 3 <-> 1 <-> 2 <-> None
dll.delete_node(dll.head.next)  # 노드 1을 삭제
dll.traverse_forward()  # Output: 2 <-> 3 <-> None
print(dll.search(2))  # Output: True
print(dll.search(4))  # Output: False