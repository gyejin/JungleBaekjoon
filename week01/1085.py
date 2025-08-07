x, y, w, h = map(int, input().split())
minWay = min(x, y, w-x, h-y)
print(minWay)
