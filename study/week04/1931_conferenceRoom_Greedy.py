import sys
input = sys.stdin.readline

N = int(input())
conference = [0] * N

for i in range(N):
    conference[i] = list(map(int, input().split()))     #회의 시작, 끝 시간 받음

conference.sort(key=lambda x:(x[1], x[0]))      #끝 시간을 기준으로 회의 정렬       (최단시간? 은 중간에 회의가 낄 수 있기에 끝시작이 좋다)

cnt = 0
last_end = 0

for start, end in conference:       #★이거 중요 리스트를 in으로 해서 각 요소를 순회할 수 있다!
    if start >= last_end:   #시작시간이 끝시간보다 크면 회의 삽입 가능
        cnt += 1
        last_end = end  #끝시간 업데이트

print(cnt)  #최대 회의 개수 출력


"""
#시간초과 직접작성
conference = [0] * N
maxTime = 0  #가장 마지막에 끝나는 회의 시간

for i in range(N):
    conference[i] = list(map(int, input().split()))     #회의 시작, 끝 시간 받기
    conference[i].append(conference[i][1] - conference[i][0])   #끝-시작 = 회의 진행 시간
    if maxTime < conference[i][1]:
        maxTime = conference[i][1]

conference.sort(key=lambda x:x[2])  #회의 진행시간이 짧은 순으로 오름차순

time = [0] * maxTime    #시간별로 리스트 생성 0으로 방문표시
total = 0

for j in range(N):
    cnt = 0
    for k in range(conference[j][0], conference[j][1]): #회의 시작~끝 시간
        if time[k] == 0:    #0이면 카운트 +1
            cnt += 1
        else:
            continue    #1이면 이 회의는 포함되지 않는 회의
    if cnt == conference[j][2]:     #회의시간과 카운트한 시간이 같으면(회의 시간을 온전히 다 쓸 수 있으면 겹치는 회의가 없으면)
        for k in range(conference[j][0], conference[j][1]):
            time[k] = 1 #해당시간 사용중으로 표시
        total += 1  #참여가능한 회의 +1

print(total)    #최대 회의 수 표시
"""