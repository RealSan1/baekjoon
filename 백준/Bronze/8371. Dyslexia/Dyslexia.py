import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = input()
B = input()
res = 0
for i in range(N):
    if A[i] != B[i]:
        res += 1

print(res)