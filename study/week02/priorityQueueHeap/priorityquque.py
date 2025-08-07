class PriorityQueue:
    def __init__(self):
        # 힙을 저장할 리스트. 0번 인덱스부터 사용.
        self.heap = []

    def push(self, item):
        """힙에 원소를 추가합니다."""
        # 1. 가장 마지막 위치에 원소를 추가
        self.heap.append(item)
        # 2. 힙 속성을 유지하기 위해 추가된 원소를 위로 올리는 작업 수행
        self._heapify_up()

    def pop(self):
        """가장 우선순위가 높은(가장 작은) 원소를 제거하고 반환합니다."""
        if not self.heap:
            return None
        # 1. 루트 노드와 마지막 노드를 교환
        self._swap(0, len(self.heap) - 1)       
        # 2. 원래 루트였던 원소(이제 마지막에 있음)를 빼냄
        min_item = self.heap.pop()    
        # 3. 새로운 루트 노드를 아래로 내리며 힙 속성을 복원
        self._heapify_down()        
        return min_item

    def _heapify_up(self):
        """가장 마지막에 추가된 원소를 부모와 비교하며 올바른 위치로 올립니다."""
        child_index = len(self.heap) - 1       
        # 자식이 루트가 아니고, 부모보다 값이 작을 동안 반복
        while child_index > 0 and self.heap[child_index] < self.heap[self._parent_index(child_index)]:
            parent_index = self._parent_index(child_index)
            self._swap(child_index, parent_index)
            child_index = parent_index

    def _heapify_down(self, index=0):
        """주어진 인덱스의 원소를 자식과 비교하며 올바른 위치로 내립니다."""
        parent_index = index        
        # 왼쪽 자식이 존재하는 동안 반복
        while self._left_child_index(parent_index) < len(self.heap):
            smallest_child_index = self._left_child_index(parent_index)
            right_child_idx = self._right_child_index(parent_index)            
            # 오른쪽 자식이 존재하고, 왼쪽 자식보다 작으면 smallest_child_index를 오른쪽으로 변경
            if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[smallest_child_index]:
                smallest_child_index = right_child_idx
            # 부모가 더 작은 자식보다 작거나 같으면 힙 속성 만족, 반복 중단
            if self.heap[parent_index] <= self.heap[smallest_child_index]:
                break                
            # 부모와 더 작은 자식의 위치를 교환
            self._swap(parent_index, smallest_child_index)
            parent_index = smallest_child_index

    # 헬퍼 함수들
    def _parent_index(self, i):
        return (i - 1) // 2
    def _left_child_index(self, i):
        return 2 * i + 1
    def _right_child_index(self, i):
        return 2 * i + 2
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def is_empty(self):
        return len(self.heap) == 0

# --- 실행 예시 ---
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push(4)
    pq.push(1)
    pq.push(7)
    pq.push(3)
    print("현재 힙 상태:", pq.heap) # 힙 속성이 유지된 리스트 출력
    print("--- pop 실행 ---")
    while not pq.is_empty():
        # 우선순위가 높은(가장 작은) 순서대로 출력됨
        print(f"Pop: {pq.pop()}, 남은 힙: {pq.heap}")
