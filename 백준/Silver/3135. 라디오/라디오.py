import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N = int(input())
arr = []
arr = {}
for _ in range(N):
    arr[int(input())] = False

arr[A] = True
result = 1001
Bool = True
for i, j in sorted(arr.items(), key=lambda x: x[0]):
    if result > abs(B-i):
        result = abs(B-i)
        Bool = j

if Bool:
    print(result)
else:
    print(result+1)