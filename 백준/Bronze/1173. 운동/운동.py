import sys
input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())

if m + T > M:
    print(-1)
    exit()

X = m
time = 0
num = 0

while num < N:
    if X + T <= M: 
        X += T
        num += 1
    else: 
        X = max(m, X - R)
    time += 1

print(time)