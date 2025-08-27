import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    D = int(input())
    S = 1
    while True:
        num = S + S**2
        if num > D:
            S -= 1
            break
        S += 1
    print(S)