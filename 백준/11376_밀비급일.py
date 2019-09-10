import sys
while True:
    test = list(sys.stdin.readline().strip('\n'))
    temp = ''.join(test)
    if temp == 'END':
        break
    test = test[::-1]
    print(*test,sep='')
