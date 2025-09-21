import sys
input = sys.stdin.readline

N = int(input())
std = list(map(str, input().split()))
arr = {}
for i in std:
    if i not in arr:
        arr[i] = 0

for _ in range(N):
    vote = list(map(str, input().split()))
    for i in vote:
        if i in arr:
            arr[i] += 1

for i in sorted(arr.items(), key=lambda x: (-x[1], x[0])):
    print(*i)