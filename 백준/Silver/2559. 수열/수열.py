N, K = map(int, input().split())
arr = list(map(int, input().split()))
result = -float("inf")
prefix = [0] * (N + 1)

for i in range(N):
    prefix[i+1] = prefix[i] + arr[i]

for i in range(N-K+1):
    result = max(result, prefix[i+K]-prefix[i])

print(result)