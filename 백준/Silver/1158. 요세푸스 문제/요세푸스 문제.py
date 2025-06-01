import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = 0
arr = [i for i in range(1, N+1)]
result = []
for i in range(N):
    num = (num + K - 1) % len(arr)
    result.append(arr.pop(num))

print('<' + str(result)[1:-1] + '>')