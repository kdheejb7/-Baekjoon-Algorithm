import sys
tree = {}  #빈 딕셔너리 생성
root = None
def preorder(root_str):
    print(root_str,end='')
    left, right = tree.get(root_str)
    if left != '.': #왼자식 존재하면
        preorder(left)
    if right != '.':
        preorder(right)
    
def inorder(root_str):
    left, right = tree.get(root_str)
    if(left != '.'):
        inorder(left)
    print(root_str,end='')
    if right != '.':
        inorder(right)
        
def postorder(root_str):
    left, right = tree.get(root_str)
    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    print(root_str,end='')
    
for _ in range(int(input())):
    info = input().strip().split(' ')
    tree[info[0]] = [info[1],info[2]]

for i in (preorder, inorder, postorder):
    i('A')
    print()
