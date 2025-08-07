import sys

input = sys.stdin.readline
#문자열 2개 받기
string_A = input().strip()  #문자열 입력 받을땐 반드시 .strip() 공백 제거!
string_B = input().strip()

#문자열 길이 미리 받기
len_A = len(string_A)
len_B = len(string_B)

LCS_list = [[0] * (len_B+1) for _ in range(len_A+1)]    #0으로 가득찬 0인덱스는 0으로 가득채운 2차원배열 만들기 

#점화식
for i in range(1, len_A+1):
    for j in range(1, len_B+1):
        #0일땐 어짜피 0으로 채워져있으니까 굳이?
        #if i == 0 or j == 0:
        #    LCS_list[i][j] = 0
        #문자열이 같을 경우
        if string_A[i-1] == string_B[j-1]:
            LCS_list[i][j] = LCS_list[i-1][j-1] + 1 #대각선 왼쪽 위 인덱스에서 +1 (이전에 받아놓은 최장 공통 부분수열 갯수에서 +1)
        #문자열이 다를 경우
        else:
            LCS_list[i][j] = max(LCS_list[i-1][j], LCS_list[i][j-1])    #같은 행-1 or 같은 열-1한 배열에서 최댓값(이전에 받아놓은 최장 공통 부분수열 갯수를 그대로 가져옴)

print(LCS_list[len_A][len_B])
