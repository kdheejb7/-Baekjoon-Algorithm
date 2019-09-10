input_value = int(input())
up = 0
down = 0
sum = 1
for i in range(1,input_value):
    sum += i
    if(sum<=input_value and sum+i+1>input_value):
        if(i%2==0):   #홀수이면
            up = i+1
            down = 1
            for j in range(input_value-sum):
                up -= 1
                down += 1
        else:
            up = 1
            down = i+1
            for j in range(input_value-sum):
                up += 1
                down -= 1
        break
print(up,'/',down,sep='')
