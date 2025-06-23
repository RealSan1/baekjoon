import sys
input = sys.stdin.readline

N, P = map(int, input().split())
W, L, G = map(int, input().split()) # 승점수 패점수 승급
info = []
res = 0
for _ in range(P):
    Name, WL = map(str, input().split())
    if WL == 'W':
        info.append(Name)

Bool = False
for _ in range(N):
    Player = input().strip()
    if Player in info:
        res += W
        if res >= G:
            Bool = True
    else:
        res -= L
        if res < 0:
            res = 0

if Bool:
    print('I AM NOT IRONMAN!!')
else:
    print('I AM IRONMAN!!')
