import sys
input = sys.stdin.readline

result = 60 * 9
H, M = map(int, input().split())

print((H * 60) + M - result)
