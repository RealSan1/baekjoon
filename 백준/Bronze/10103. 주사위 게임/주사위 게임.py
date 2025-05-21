import sys
input = sys.stdin.readline

CHAG, SANG = 100, 100
N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    if A > B:
        SANG -= A
    elif A < B:
        CHAG -= B
    elif A == B:
        pass

print(CHAG)
print(SANG)