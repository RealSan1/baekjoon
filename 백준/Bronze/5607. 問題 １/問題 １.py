import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
Ares = Bres = 0
for _ in range(N):
    A, B = map(int, input().split())
    if A > B:
        Ares += A+B
    elif A < B:
        Bres += A+B
    elif A == B:
        Ares += A
        Bres += B

print(Ares, Bres)