import sys
input = lambda: sys.stdin.readline().rstrip()

X1, Y1, R1 = map(int, input().split())
X2, Y2, R2 = map(int, input().split())

if (R1 + R2) ** 2 > (X2 - X1) ** 2 + (Y2 - Y1) ** 2:
    print("YES")
else:
    print("NO")