import sys
input = sys.stdin.readline

N = input().strip()
res = 0

for i in N:
    res += int(i) ** 5

print(res)