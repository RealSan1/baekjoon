import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    input()
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(int(input()))
    if sum(arr) % N == 0:
        print('YES')
    else:
        print('NO')