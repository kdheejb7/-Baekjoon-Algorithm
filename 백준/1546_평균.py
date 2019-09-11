count = int(input())
score = list(map(int, input().split()))
score.sort()
sum = 0
for i in score:
    sum += (i/score[-1]*100)
print(sum/len(score))
