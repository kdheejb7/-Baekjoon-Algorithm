for _ in range(int(input())):
    scoreList = list(map(int,input().split()))
    average = sum(scoreList[1:])/scoreList[0]
    print("%0.3f"%round(len([i for i in scoreList[1:] if i > average])/scoreList[0]*100, 3),'%',sep='')
   
