import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

if N == 1:
    print(min(arr)**2)
else:
    print(min(arr) * max(arr))