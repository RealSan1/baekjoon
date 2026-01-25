import sys
input = lambda: sys.stdin.readline().rstrip()

a, b, c, d, e, f = map(int, input().split())
A = set()
B = set()
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            exit()
