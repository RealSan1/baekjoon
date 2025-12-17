import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
res = 0
for i in map(int, input().split()):
    if N == i:
        res += 1

print(res)