import itertools
while True:
    q = list(map(int, input().split()))
    if q==[0]:
        break
    number = q.pop(0)
    answer = list(itertools.combinations(q,6))
    for i in answer:
        print(*i, sep=' ')
    print()
'''
first_list = q[0:6]
temp_list=q[6:]
answer_list = []
for i in temp_list:
    for j in range(6):
        mylist = first_list.copy()
        mylist[j] = i
        answer_list.append(mylist)
for i in range(len(answer_list)):
    answer_list[i].sort()
answer_list.sort()
print(*answer_list,sep='\n')
'''
'''
while True:
    temp = list(q[:6])
    if temp in answer_list:
        break
    answer_list.append(temp)
    q.append(q.pop(0))
for i in range(len(answer_list)):
    answer_list[i].sort()
answer_list.sort()
for i in range(len(answer_list)):
    print(*answer_list[i], sep=' ')
'''
