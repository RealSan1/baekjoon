import math
T = int(input())
arr = []
dp = []
for i in range(T):
    arr.append(float(input()))
    if i == 0:
        dp.append(arr[0])
    else:
        dp.append(max(dp[i-1] * arr[i], arr[i]) )

result = max(dp)
print("%.3f"%result)


    