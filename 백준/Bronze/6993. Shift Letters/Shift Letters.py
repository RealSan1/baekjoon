import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    A, B = map(str, input().split())
    B = int(B)
    res = A[-B:] + A[:-B]
    print(f"Shifting {A} by {B} positions gives us: {res}")