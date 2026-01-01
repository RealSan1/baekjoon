import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = {i : 0 for i in range(1, N+1)}

for i in range(M):
    A, B = map(int, input().split())
    arr[A] += 1
    arr[B] += 1

for i, j in arr.items():
    print(j)