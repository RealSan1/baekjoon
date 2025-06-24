import sys
input = sys.stdin.readline

arr = {}
for _ in range(5):
    A = int(input())
    if A in arr:
        arr[A] += 1
    else:
        arr[A] = 1

res = 0
for i,j in arr.items():
    if j % 2 == 1:
        print(i)
