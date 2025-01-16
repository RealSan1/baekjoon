import sys
input = sys.stdin.readline

N = int(input())
arr = {}
for _ in range(N):
    A = int(input())
    if A in arr:
        arr[A] += 1
    else:
        arr[A] = 0

A = dict(sorted(arr.items(), key=lambda x: x[0])) # 정렬

print(max(A, key=A.get))