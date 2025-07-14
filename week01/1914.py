"""
N = int(input())
t1 = []
t2 = []
t3 = []

for i in range(N, 0, -1):
    t1.append(i)

while True:
    if t3
"""
def hanoi(n, start, end, aux):
    if n == 1:
        print(start, end)
        return

    hanoi(n-1, start, aux, end)
    print(start, end)
    hanoi(n-1, aux, end, start)

N = int(input())
print(2**N-1)

if N <= 20:
    hanoi(N, 1, 3, 2)
