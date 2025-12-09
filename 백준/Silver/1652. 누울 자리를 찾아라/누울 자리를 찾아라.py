import sys
input = lambda: sys.stdin.readline().rstrip()

room = []
N = int(input())
for i in range(N):
    room.append(input())

room_rotate = [[0] * N for _ in range(N)]
garo = sero = 0
for i in room:
    for j in i.split('X'):
        if len(j) >= 2:
            garo += 1

for i in range(N):
    for j in range(N):
        room_rotate[j][N-1-i] = room[i][j]

for i in room_rotate:
    num = ''
    for j in i:
        num += j
    for sp in num.split('X'):
        if len(sp) >= 2:
            sero += 1

print(garo, sero)