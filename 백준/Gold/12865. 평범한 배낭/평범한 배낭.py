import sys

input= sys.stdin.readline
N, K = map(int, input().split()) #물품 수/무게
stuff = []
dp = [0 for _ in range(K+1)]

for _ in range(N):
    W, V = map(int, input().split()) #물건의 무게/가치
    stuff.append([W, V])


for W, V in stuff:
    for i in range(K, W-1, -1):
        dp[i] = max(dp[i], dp[i-W]+V)

print(dp[-1])