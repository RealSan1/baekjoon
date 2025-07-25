import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(input().strip())

if sorted(arr) == arr:
    print("INCREASING")
elif sorted(arr, reverse=True) == arr:
    print("DECREASING")
else:
    print("NEITHER")