N = int(input())


for i in range(N):
    string = ''
    R, S = input().split()
    for j in range(len(S)):
        string += S[j] * int(R)
    print(string)
