import sys
input = sys.stdin.readline

arr = {}
N, M = map(int, input().split())
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word in arr:
            arr[word] += 1
        else:
            arr[word] = 1

sort = sorted(arr.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for key, value in sort:
    print(key)