import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = list(map(int, input().split()))

temp = sum(data[:K])
maxsum = temp

for i in range(K, N):
    temp = temp - data[i-K] + data[i]
    maxsum = max(maxsum, temp)

print(maxsum)