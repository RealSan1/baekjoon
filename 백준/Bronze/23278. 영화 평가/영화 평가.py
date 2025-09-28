import sys
input = lambda: sys.stdin.readline().rstrip()

N, L, H = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in range(L):
    arr.pop(0)

for i in range(H):
    arr.pop(-1)

print(sum(arr) / len(arr))