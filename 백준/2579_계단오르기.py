stairCount = int(input())
arr = []
for i in range(stairCount):
    arr.append(int(input()))
maxSum = [0]*stairCount
if stairCount == 1:
    print(arr[0])
elif stairCount == 2:
    print(arr[0]+arr[1])
else:
    maxSum[0] = arr[0]
    maxSum[1] = arr[0] + arr[1]
    maxSum[2] = max(maxSum[0]+arr[2], arr[1]+arr[2])
    for i in range(3,stairCount):
        maxSum[i] = max(maxSum[i-2]+arr[i], maxSum[i-3]+arr[i-1]+arr[i])
print(maxSum[stairCount-1])
