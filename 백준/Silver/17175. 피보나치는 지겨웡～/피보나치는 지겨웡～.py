import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)
try:
    dp[0] = 1
    dp[1] = 1
except:
    dp[0] = 1

for i in range(2, N+1):
    dp[i] = (dp[i-1] + dp[i-2] + 1) % 1000000007

print(dp[N])