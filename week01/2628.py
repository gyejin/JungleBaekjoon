"""
width, length = map(int, input().split())
cut = int(input())
cutting = []

for i in range(cut):
    cutting.append(list(input().split()))

wid = []
leng = []
widF = []
lengF = []
for j in range(cut):
    if cutting[j][0] == '0':
        leng.append(cutting[j][1])
    else:
        wid.append(cutting[j][1])

leng = list(map(int, leng))
wid = list(map(int, wid))

lengF.append(length - max(leng))
lengF.append(min(leng))
for k in range(len(leng)):
    if (k+1) < len(leng):
        lengF.append(abs(leng[k]-leng[k+1]))
    else:
        break

widF.append(width - max(wid))
widF.append(min(wid))
for o in range(len(wid)):
    if (o+1) < len(wid):
        widF.append(abs(wid[o]-wid[o+1]))
    else:
        break

print(max(lengF) * max(widF))

#max는 가로길이랑, min은 0이랑 차, 나머진 지네끼리 해서 abs 젤 높은 거
"""

width, height = map(int, input().split())
num_cuts = int(input())

# 0과 전체 길이를 미리 넣어둠
horizontal_cuts = [0, height]
vertical_cuts = [0, width]

for _ in range(num_cuts):
    direction, position = map(int, input().split())     #이렇게 split으로 받아도 되네! 리스트말고!
    if direction == 0: # 가로로 자르는 경우 (높이에 영향)
        horizontal_cuts.append(position)
    else: # 세로로 자르는 경우 (너비에 영향)
        vertical_cuts.append(position)

# 정렬!
horizontal_cuts.sort()
vertical_cuts.sort()

max_height = 0
for i in range(1, len(horizontal_cuts)):
    # 정렬된 리스트에서 인접한 값의 차이가 각 조각의 높이
    h = horizontal_cuts[i] - horizontal_cuts[i-1]       #이렇게 거꾸로 받아오는게 에러에 효율적
    if h > max_height:
        max_height = h

max_width = 0
for i in range(1, len(vertical_cuts)):
    # 정렬된 리스트에서 인접한 값의 차이가 각 조각의 너비
    w = vertical_cuts[i] - vertical_cuts[i-1]
    if w > max_width:
        max_width = w

print(max_height * max_width)

