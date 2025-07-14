import math
A, B, V = map(int, input().split())

days = math.ceil((V-B) / (A-B))
print(days)

"""
A, B, V = map(int, input().split())
day = 0
way = 0
while(1):
    day += 1
    way += A
    if way >= V:
        break
    way -= B
print(day)
"""
