import sys
input = sys.stdin.readline

N = int(input())
arr = set()
for _ in range(N):
    A = int(input())
    arr.add(A)
arr = sorted(arr, reverse=True)

for i in arr:
    print(i)