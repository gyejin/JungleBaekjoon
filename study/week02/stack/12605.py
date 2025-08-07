import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    word = list(input().split())
    print(f'Case #{i+1}: ', end='')
    for j in range(len(word)):
        print(word[-(j+1)], end=' ')
    print()

    #word.reverse() #리스트 뒤집기
    #reversed_word = word[::-1] # 뒤집힌 새로운 리스트 생성
    #print(' '.join(reversed_word))