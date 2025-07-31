import sys
input = sys.stdin.readline

N = int(input())
arr = list(range(N, 0, -1))
print(*arr)