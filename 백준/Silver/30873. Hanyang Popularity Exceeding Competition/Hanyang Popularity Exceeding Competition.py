import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
X = 0
for n in range(N):
    P, C = map(int, input().split())
    if abs(P-X) <= C:
        X += 1

print(X)