import sys

input = sys.stdin.readline
N = int(input())
tree = {}   #트리를 루트:왼쪽,오른쪽으로 구성

for _ in range(N):
    root, left, right = input().strip().split()     #문자열 나눠서 받기 sys사용시 문자열 입력받을 땐 \n개행 제거 필수!(int는 자동 제거) 
    tree[root] = [left,right]   #루트와 왼쪽,오른쪽 키값쌍으로 받음

def preorder(root):
    if root != '.':     #루트가 비지 않았으면
        print(root, end='')     #루트   V
        preorder(tree[root][0]) #왼쪽   L
        preorder(tree[root][1]) #오른쪽 R

def inorder(root):
    if root != '.':
        inorder(tree[root][0])  #왼쪽   L
        print(root, end='')     #루트   V
        inorder(tree[root][1])  #오른쪽 R

def postorder(root):
    if root != '.':
        postorder(tree[root][0])    #왼쪽   L
        postorder(tree[root][1])    #오른쪽 R
        print(root, end='')         #루트   V

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()