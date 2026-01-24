import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
res = 0
for A in range(1, 501):
    for B in range(1, 501):
        if A ** 2 == (B ** 2) + N:
            res += 1

print(res)