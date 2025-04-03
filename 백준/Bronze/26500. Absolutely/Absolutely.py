import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    A, B = map(float, input().split())
    print(f"{abs(A-B):.1f}")