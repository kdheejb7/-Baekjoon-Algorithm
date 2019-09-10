import sys
mylist = []
stack = []
for _ in range(int(input())):
    mylist.append(list(sys.stdin.readline().split()))
for i in mylist:
    if i[0] == 'push':
        stack.append(int(i[1]))
    elif i[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif i[0] == 'size':
        print(len(stack))
    elif i[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif i[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
