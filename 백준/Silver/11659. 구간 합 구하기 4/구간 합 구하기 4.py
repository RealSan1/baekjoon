import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

prefixSum = [0] * (N + 1)
for i in range(1, N + 1):
    prefixSum[i] = prefixSum[i-1] + arr[i-1]

for _ in range(M):
    I, J = map(int, input().split())
    print(prefixSum[J] - prefixSum[I-1])
