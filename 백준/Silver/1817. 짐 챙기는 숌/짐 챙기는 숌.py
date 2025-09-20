import sys
input = sys.stdin.readline

N, M = map(int, input().split())
if N == 0:
    print(0)
    sys.exit()

weight = list(map(int, input().split()))

box = 0
num = 0
for w in weight:
    if num + w <= M:
        num += w
    else:
        box += 1 
        num = w 

if num > 0:
    box += 1

print(box)
