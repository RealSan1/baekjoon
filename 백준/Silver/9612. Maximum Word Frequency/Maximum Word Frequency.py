import sys
input = sys.stdin.readline

T = int(input())
arr = {}
for _ in range(T):
    num = input().strip()
    if num in arr:
        arr[num] += 1
    else:
        arr[num] = 1

sort = sorted(arr.items(), key=lambda x: (x[1], x[0]), reverse=True)
print(sort[0][0], sort[0][1])