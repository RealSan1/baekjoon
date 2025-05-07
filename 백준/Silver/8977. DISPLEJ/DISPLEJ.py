import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
arr = list(map(int, input().split()))
index = (B % N) - 1
result = 0
for i in range(K):
    if index >= N:
        index = 0
    result += arr[index]
    index += 1

print(result)