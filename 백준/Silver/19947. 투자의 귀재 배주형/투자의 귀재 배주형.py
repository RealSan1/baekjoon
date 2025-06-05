import sys
input = sys.stdin.readline

H, Y = map(int, input().split())
dp = [H] * (Y+1)
for i in range(1, Y+1):
    V = [int(dp[i-1] * 1.05)]
    if i > 2:
        V.append(int(dp[i-3] * 1.20))
    if i > 4:
        V.append(int(dp[i-5] * 1.35))
    dp[i] = max(V)

print(dp[-1])