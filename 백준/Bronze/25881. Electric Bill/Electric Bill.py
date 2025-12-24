import sys
input = sys.stdin.readline

A, B = map(int, input().split())
for i in range(int(input())):
    H = int(input())
    if H > 1000:
        print(H, (1000 * A) + ((H - 1000) * B))
    else:
        print(H, H * A)