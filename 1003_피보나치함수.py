caseCount = int(input()) #입력받기

def zero_one_count(value):
    zero_count = [1,0]
    one_count = [0,1]
    if value == 0 :
        print("%d %d"%(zero_count[0],one_count[0]))
    elif value == 1:
        print("%d %d"%(zero_count[1],one_count[1]))
    else:
        for j in range(2,value+1):
            zero_count.append(zero_count[j-2]+zero_count[j-1])
            one_count.append(one_count[j-2]+one_count[j-1])
        print("%d %d" %(zero_count[value],one_count[value]))
    
for i in range(0,caseCount):
    value = int(input())    #입력받기
    zero_one_count(value)
