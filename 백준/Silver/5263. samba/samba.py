import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = {}
for _ in range(N):
    ID = int(input())
    if ID in arr:
        arr[ID] += 1
    else:
        arr[ID] = 1

for i, j in arr.items():
    if j % K != 0:
        print(i)
        break