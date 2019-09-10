import sys
ans_pre=[]
ans_in=[]
ans_post=[]
tree = {}  #빈 딕셔너리 생성
root = None
def preorder(root_str):
    ans_pre.append(root_str)
    left, right = tree.get(root_str)
    if left != '.': #왼자식 존재하면
        preorder(left)
    if right != '.':
        preorder(right)
    
def inorder(root_str):
    left, right = tree.get(root_str)
    if(left != '.'):
        inorder(left)
    ans_in.append(root_str)
    if right != '.':
        inorder(right)
        
def postorder(root_str):
    left, right = tree.get(root_str)
    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    ans_post.append(root_str)
    
for _ in range(int(input())):
    info = input().strip().split(' ')
    tree[info[0]] = [info[1],info[2]]
preorder('A')
inorder('A')
postorder('A')
print(*ans_pre,sep='')
print(*ans_in,sep='')
print(*ans_post,sep='')
