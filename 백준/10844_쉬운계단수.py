num = int(input())
dp = [[0 for col in range(10)] for row in range(num)]
for i in range(1,10):
    dp[0][i] = 1
for i in range(1,num):
    dp[i][0] = dp[i-1][1]
    for j in range (1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][9] = dp[i-1][8]

sum = 0
for i in range(10):
    sum += dp[num-1][i]
    
print(sum%1000000000)
