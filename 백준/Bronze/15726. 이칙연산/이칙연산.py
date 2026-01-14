import sys
input = lambda: sys.stdin.readline().rstrip()

N = list(map(int, input().split()))

print(max(int(N[0] / N[1] * N[2]), int(N[0] * N[1] / N[2])))