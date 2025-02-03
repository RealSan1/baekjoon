import sys
input = sys.stdin.readline

dp = [0] * 1001

dp[1], dp[2] = 1, 2

N = int(input())
for i in range(3, N+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[N] % 10007)