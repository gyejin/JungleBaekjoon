import sys

input = sys.stdin.readline
N = int(input())

for i in range(N):
    parentheses = input()
    stack = []
    is_true = True      #스택이 비어있는지 확인용
    for chr in parentheses:     #문자열 순회하면서 비교
        if chr == '(':
            stack.append(chr)   # ( 는 stack에 저장
        elif chr == ')':        # ) 는 두가지, 스택이 비어있으면 처음들어온게 )는 불가, 스택에 (있으면 '('를 pop
            if not stack:
                is_true = False
                break
            stack.pop() #굳이 stack에 넣지 않음 넣으면 괜히 꼬이기만 하니까 비교용으로만!
    if stack:   #stack이 true
        is_true = False
    
    if is_true:
        print("YES")
    else:
        print("NO")
"""
for i in range(N):
    stack = input()
    for j in range(len(stack)):
        if stack[0] == ')':
            print("NO")
        elif stack[0] == '(':
            if j == 0:
                continue
            if stack[j-1] == '(' and stack[j] == ')':
                stack.pop()
                stack.pop()
"""
