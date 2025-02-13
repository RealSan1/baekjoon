import sys
input = sys.stdin.readline

K, L = map(int, input().split())

arr = {}
for _ in range(L):
    A = input().strip()
    if A in arr:
        arr.pop(A)
    arr[A] = 0

temp = 0
for i, j in arr.items():
    if temp < K:
        print(i)
    else:
        break
    temp += 1
