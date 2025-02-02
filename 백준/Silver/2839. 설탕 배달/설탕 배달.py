import sys, math
input = sys.stdin.readline
MAX = sys.maxsize

dp = [MAX] * 5001

dp[3], dp[5] = 1, 1

n = int(input())
for i in range(6, n+1):
    dp[i] = min(dp[i], dp[i-3] + 1, dp[i-5] + 1)

if dp[n] == MAX:
    print(-1)
else:
    print(dp[n])