number = int(input())
count = 0

if number < 100:
    print(number)
else: #무조건 세자리수
    for i in range(100,number+1):
        tmpList = list(str(i))       
        tmpList = list(map(int,tmpList))
        if tmpList[2]-tmpList[1] == tmpList[1]-tmpList[0]:
            count += 1

    print(99 + count)
