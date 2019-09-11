def check_stack(list):
    temp = []
    for i in list:
        if i == '(':
            temp.append(i)
        else:
            if temp:
                temp.pop()
            else:
                return 'NO'
    if temp:
        return 'NO'
    else:
        return 'YES'

answer = []
for _ in range(int(input())):
    list2 = list(input())
    answer.append(check_stack(list2))

print(*answer,sep='\n')    
 
