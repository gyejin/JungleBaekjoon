T = int(input())
a = 0
hap = 0

for i in range(T):
    OX = input()
    L = len(OX)
    listOX = list(OX)
    for j in range(L):
        if listOX[j] == 'O':
            a += 1
            hap += a
        elif listOX[j] == 'X':
            a = 0
    print(hap)
    hap = 0
    a = 0

T = int(input())

######################################
for _ in range(T):
    # 변수를 루프 시작 시점에 초기화
    score = 0
    streak = 0

    ox_string = input()

    # 문자열을 직접 순회
    for char in ox_string:
        if char == 'O':
            streak += 1
            score += streak
        else: # char == 'X'
            streak = 0

    print(score)
