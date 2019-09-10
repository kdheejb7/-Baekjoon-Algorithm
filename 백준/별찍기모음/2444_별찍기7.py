count = int(input())
for i in range(1,count*2):
    print(' '*abs(count-i),end='')
    if(i<=count):
        print('*'*(2*i-1))
    else:
        print('*'*(2*(count*2-i)-1))
count = int(input())
for i in range(1,count*2):
    print(' '*abs(count-i),end='')
    print('*'*(2*(count-abs(count-i))-1))
