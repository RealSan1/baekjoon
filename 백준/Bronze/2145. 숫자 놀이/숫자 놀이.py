import sys
input = sys.stdin.readline

while True:
    N = list(map(int, input().strip()))
    if N[0] == 0:
        break

    while len(N) != 1:
        N = sum(N)
        N = list(map(int, str(N)))

    print(*N)