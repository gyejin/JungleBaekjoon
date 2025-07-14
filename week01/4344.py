C = int(input())

for i in range(C):
    hap = 0
    stud = 0
    numScore = list(map(int, input().split()))
    for j in range(1, numScore[0]+1):
        hap += numScore[j]
    average = hap / numScore[0]

    for k in range(1, numScore[0]+1):
        if numScore[k] > average:
            stud += 1
    perc = float((stud / numScore[0]) * 100)
    perC = round(perc, 3)
    print('{:.3f}%'.format(perC))
        
"""
C = int(input())

for _ in range(C):
    data = list(map(int, input().split()))
    N = data[0]       # 첫 번째 값은 학생 수
    scores = data[1:]   # 두 번째 값부터 끝까지는 점수 (슬라이싱)

    average = sum(scores) / N # sum()으로 간단하게 평균 계산

    # 평균 넘는 학생 수 계산
    above_avg_count = 0
    for score in scores:
        if score > average:
            above_avg_count += 1

    # 비율 계산 및 출력 형식 지정
    ratio = (above_avg_count / N) * 100
    print(f'{ratio:.3f}%') # f-string을 이용한 깔끔한 형식 지정
"""
