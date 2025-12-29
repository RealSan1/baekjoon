import sys
input = lambda: sys.stdin.readline().rstrip()


for t in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    P = list(map(int, input().split()))

    order = sorted( range(N), key=lambda i: (-(P[i] / L[i]), i))

    print(f"Case #{t+1}: {' '.join(map(str, order))}")