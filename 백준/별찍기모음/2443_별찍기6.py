count = int(input())
for i in range(count,0,-1):
    print(' '*(count-i),end='')
    print('*'*(2*i-1))
