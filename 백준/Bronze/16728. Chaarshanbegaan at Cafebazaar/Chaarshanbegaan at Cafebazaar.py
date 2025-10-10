import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
res = 0
for _ in range(N):
    X, Y = map(int, input().split())
    D = (X ** 2 + Y ** 2) ** 0.5
    if D <= 10:
        res += 10
    elif 10 < D <= 30:
        res += 9
    elif 30 < D <= 50:
        res += 8
    elif 50 < D <= 70:
        res += 7
    elif 70 < D <= 90:
        res += 6
    elif 90 < D <= 110:
        res += 5
    elif 110 < D <= 130:
        res += 4
    elif 130 < D <= 150:
        res += 3
    elif 150 < D <= 170:
        res += 2
    elif 170 < D <= 190:
        res += 1
    elif 190 < D:
        res += 0

print(res)