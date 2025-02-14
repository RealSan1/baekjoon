import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 1001

dp[0] = (0, 1)
dp[1] = (0, 1)
dp[2] = (2, 1)

for i in range(2, N+1):
    dp[i] = (dp[i-1][1] * 2, sum(dp[i-1]))

print(sum(dp[N]) % 10007)