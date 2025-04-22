import sys
input = sys.stdin.readline

info = {}
N = int(input())
for _ in range(N*2-1):
    name = input().strip()
    if name in info:
        info.pop(name)
    else:
        info[name] = None

for i in info.keys():
    print(i)