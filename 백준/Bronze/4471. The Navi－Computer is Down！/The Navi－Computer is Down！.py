import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
for _ in range(N):
    A = input()
    Ax, Ay, Az = map(float, input().split())

    B = input()
    Bx, By, Bz = map(float, input().split())

    res = ((Bx - Ax) ** 2 + (By - Ay) ** 2  + (Bz - Az) ** 2 ) ** 0.5
    print(f"{A} to {B}: {res:.2f}")