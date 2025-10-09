import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = 0
for i in range(N):
    if B[i] == 1:
        continue
    else:
        res += A[i]

print(sum(A))
print(res)