import sys
input = sys.stdin.readline

T = int(input())
arr = []
for _ in range(T):
    A = int(input())
    arr.append(A)

arr.sort()
for i in arr:
    print(i)