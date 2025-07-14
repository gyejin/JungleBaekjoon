"""
sosu = []
for i in range(1, 10001):
    cnt = 1
    for j in range(2, 10001):
        if i % j == 0:
            cnt += 1
        elif i < j:
            break
    if cnt == 2:
        sosu.append(i)

print(sosu)
"""

import sys
import math

is_prime_list = [True] * 10001
is_prime_list[0] = is_prime_list[1] = False
for i in range(2, int(math.sqrt(10001)) + 1):
    if is_prime_list[i]:
        for j in range(i * i, 10001, i):
            is_prime_list[j] = False

sosu = []
for i in range(len(is_prime_list)):
    if is_prime_list[i]:
        sosu.append(i)


T = int(input())
for k in range(T):
    GP1 = []
    GP2 = []
    cha = []
    num = int(input())
    for h in sosu:
        for o in sosu:
            if num == (h+o):
                GP1.append(h)
                GP2.append(o)
            elif o >= num:
                break
        if h >= num:
            break
    for p in range(len(GP1)):
        cha.append(abs(GP1[p] - GP2[p]))
        """
        if GP1[p] > GP2[p]:
            cha.append(GP1[p] - GP2[p])
        elif GP1[p] == GP2[p]:
            cha.append(0)
        else:
            cha.append(GP2[p] - GP1[p])
        """
    ind = cha.index(min(cha))
    sort = sorted([GP1[ind], GP2[ind]])
    print(sort[0], sort[1])
        

