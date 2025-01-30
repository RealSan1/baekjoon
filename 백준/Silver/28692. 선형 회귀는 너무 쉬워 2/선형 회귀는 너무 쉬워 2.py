import sys
input = sys.stdin.readline

n = int(input())
Sx, Sy, Sxx, Sxy, = 0, 0, 0, 0
for _ in range(n):
    x, y = map(int, input().split())
    Sx += x
    Sy += y
    Sxx += x**2
    Sxy += x*y

try:
    a2 = (n * Sxy - Sx * Sy) / (n * Sxx - (Sx ** 2))
    b2 = (Sy - (a2 * Sx)) / n
    print(f"{a2} {b2}")
except:
    print('EZPZ')