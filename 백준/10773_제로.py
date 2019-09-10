import sys
mylist = []
stack = []
for _ in range(int(input())):
    mylist.append(int(sys.stdin.readline()))
for i in mylist:
    if not i: #0이면
        stack.pop()
    else:
        stack.append(i)
print(sum(stack))
