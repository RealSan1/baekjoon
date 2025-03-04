import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
data = {}
for i in arr:
    if i in data:
        data[i] += 1
    else:
        data[i] = 1

print(max(data.values()))