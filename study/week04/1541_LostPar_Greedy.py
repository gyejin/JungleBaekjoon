import sys
input = sys.stdin.readline

num = list(input().strip().split('-'))

subHaptot = 0
for i in range(len(num)):
    numHapList = map(int,num[i].split('+'))
    if i == 0:
        numHap = sum(numHapList)
    else:
        subHap = sum(numHapList)
        subHaptot += subHap
print(numHap - subHaptot)

"""
#Gem답
import sys
input = sys.stdin.readline

# '-'를 기준으로 식을 나눈다.
parts = input().strip().split('-')

# 첫 번째 부분은 '+'로 쪼개서 미리 더해둔다.
result = sum(map(int, parts[0].split('+')))

# 두 번째 부분부터는 반복문으로 돌면서, 각 부분을 합산한 뒤 전체 결과에서 빼준다.
for i in range(1, len(parts)):
    part_sum = sum(map(int, parts[i].split('+')))
    result -= part_sum
    
print(result)
"""