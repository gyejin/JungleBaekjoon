import sys

nan = [int(sys.stdin.readline()) for _ in range(9)]
#nan = []
#for _ in range(9):
#    nan.append(int(sys.stdin.readline()))

total_height = sum(nan)
spy_height_hap = total_height - 100

spy1, spy2 = 0, 0

for i in range(9):
    for j in range(i+1, 9):
        if nan[i] + nan[j] == spy_height_hap:
            spy1 = nan[i]
            spy2 = nan[j]
            break
    if spy1:
        break
    
nan.remove(spy1)
nan.remove(spy2)

nan.sort()
for height in nan:
    print(height)

"""
백트래킹
import sys

# 9명의 키를 입력받고 정렬
# 미리 정렬해두면, 나중에 찾았을 때 바로 출력할 수 있어요.
dwarfs = sorted([int(sys.stdin.readline()) for _ in range(9)])

# 결과를 저장할 리스트
result = []

def find_seven_dwarfs(start_index, selected):
    # 전역 변수 result를 사용하겠다고 선언
    global result
    
    # 이미 정답을 찾았다면 더 이상 탐색하지 않음
    if result:
        return

    #  sétimo 난쟁이를 선택했다면
    if len(selected) == 7:
        # 키의 합이 100인지 확인
        if sum(selected) == 100:
            # 정답을 찾았으므로 결과 저장
            result = selected
        return

    # start_index부터 9번째 난쟁이까지 탐색
    for i in range(start_index, 9):
        # i번째 난쟁이를 선택하고
        selected.append(dwarfs[i])
        
        # 재귀 호출: 다음 난쟁이는 i+1부터 탐색
        find_seven_dwarfs(i + 1, selected)
        
        # 백트래킹: i번째 난쟁이를 선택하지 않은 경우를 위해 리스트에서 제거
        selected.pop()

# 백트래킹 함수 시작
find_seven_dwarfs(0, [])

# 결과 출력
for height in result:
    print(height)
"""
