import sys, math
input = sys.stdin.readline

dp = [0] * 10001
dp[1], dp[2] = 1, 1

n = int(input())
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])