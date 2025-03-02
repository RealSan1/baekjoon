import sys
input = sys.stdin.readline

dp = [0] * 4788
dp[0] = 0
dp[1] = 1

N = int(input())
for i in range(2, N+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[N])