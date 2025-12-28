import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = []
for _ in range(N):
    A = input()
    A = sorted(A)
    if A not in arr:
        arr.append(A)

print(len(arr))