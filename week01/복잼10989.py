import sys
N = int(sys.stdin.readline())
sortNum = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    sortNum[num] += 1

for i in range(1, 10001):
    for j in range(sortNum[i]):
        print(i)

"""
"일단 정렬이네? list.sort()를 써볼까?"
→ "아, 근데 N이 천만이고 메모리가 8MB네. num_list = [] 하는 순간 메모리 초과 나겠다. 이 방법은 절대 안돼."

"그럼 숫자를 저장하지 않고 정렬할 방법이 있나? 다른 조건이 뭐지?"
→ "수가 1부터 10000 사이구나! 아하! 숫자 종류는 1만 개밖에 안 되네. 그렇다면 각 숫자가 몇 개 나왔는지 개수만 세면 되겠다!"

"계획을 세워보자."
a. 먼저, 10001칸짜리 0으로 채워진 리스트 counts를 만들어야겠다. counts = [0] * 10001
b. N번 반복하면서 숫자를 하나씩 읽어야지. for _ in range(N):
c. 읽은 숫자를 num이라고 하면, counts[num] += 1 이렇게 개수만 세고, 읽은 숫자는 바로 버리자.
d. 입력이 다 끝나면, 이제 counts 리스트를 1번부터 10000번까지 훑으면서 결과를 출력해야 해. for i in range(1, 10001):
e. 만약 counts[i]가 3이라면, i를 3번 출력하면 되겠네. for j in range(counts[i]): print(i)

이 생각의 흐름을 코드로 옮기면 바로 정답이 되는 거야.
"""
