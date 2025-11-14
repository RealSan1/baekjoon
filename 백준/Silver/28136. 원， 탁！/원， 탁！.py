import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

res = 0
for i in range(N):
    if arr[i] >= arr[(i+1) % N]:
        res += 1

print(res)
