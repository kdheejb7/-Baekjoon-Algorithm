num1,num2 = map(int,input().split())
tmp_gcm = num1*num2
while num2 != 0:
    tmp = num1 % num2
    num1 = num2
    num2 = tmp

print(num1)
print(tmp_gcm//num1)
