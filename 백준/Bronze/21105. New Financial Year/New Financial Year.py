import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    P, C = map(float, input().split())
    O = P / ((C / 100) + 1)
    print(f"{O:.9f}")