import sys
input = sys.stdin.readline

T = int(input())
pi = 3.14159
res = 0
for _ in range(T):
    V = list(map(str, input().split()))
    if V[0] == 'C':
        R, H = float(V[1]), float(V[2])
        res = max(res, (1/3)*(pi*R*R*H))
    elif V[0] == 'L':
        R, H = float(V[1]), float(V[2])
        res = max(res, pi*R*R*H)
    elif V[0] == 'S':
        R = float(V[1])
        res = max(res, (4/3)*pi*R*R*R)

print(f"{res:.3f}")