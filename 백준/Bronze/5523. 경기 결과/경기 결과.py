import sys
input = sys.stdin.readline

N = int(input())
A1 = 0
B1 = 0
for _ in range(N):
    A, B = map(int, input().split())
    if A > B:
        A1 += 1
    elif A < B:
        B1 += 1
    elif A == B:
        pass

print(A1, B1)