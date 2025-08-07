num = []
for i in range(0, 9):
    a = int(input())
    num.append(a)

big = max(num)      #2번 이상 쓸거면 시간복잡도 상 변수 저장해놓고 쓰는게 좋음
print(big)
print(num.index(big) + 1)

#print(max(num))
#print(num.index(max(num)) + 1)
