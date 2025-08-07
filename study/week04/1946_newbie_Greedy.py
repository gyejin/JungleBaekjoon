import sys
input = sys.stdin.readline

#서류 1등은 무조건 뽑고 점수 입력받을때 서류 1등보다 낮은 면접 점수를 가지 지원자 그때그때 합격 -> 이게 무슨
T = int(input())

for _ in range(T):
    cnt = 1
    N = int(input())
    volunteer = [0] * N
    for i in range(N):
        volunteer[i] = list(map(int,input().split()))   #지원자의 서류점수, 면접점수 받기
        
    volunteer.sort()    #서류 1등부터 정렬 -> 2차원 배열에서 sort하면 앞 인덱스 기준으로 정렬
    
    interview_LimitScore = volunteer[0][1]  #면접 하한선

    for j in range(1, N):
        if volunteer[j][1] < interview_LimitScore:  #면접 점수가 서류1등 보다 좋으면
            cnt += 1    #합격
            interview_LimitScore = volunteer[j][1]  #합격한 사람의 면접점수로 대체
    print(cnt)

"""
#전체 입력받고 합격여부 결정 -> 아니 이게 진정한 채용프로세스 아님?
for _ in range(T):
    cnt = 2
    N = int(input())
    volunteer = [0] * N
    for i in range(N):
        volunteer[i] = list(map(int,input().split()))
        if volunteer[i][0] == 1:
            interview_score = volunteer[i][1]
        elif volunteer[i][1] == 1:
            doc_score = volunteer[i][0]
    
    for j in range(N):
        if volunteer[j][0] < doc_score and volunteer[j][1] < interview_score:
            cnt += 1

    print(cnt)
"""