caseCount = int(input())    #입력 받기
output = []
output.insert(0,0)
output.insert(1,1)
output.insert(2,2)
output.insert(3,4)

for i in range(0,caseCount):
    value = int(input())    #입력 받기
    if value <= 3:
        print(output[value])
    else:
        for j in range(4, value+1):
            temp = output[j-3]+output[j-2]+output[j-1]
            output.insert(j,temp)
        print(output[value])
