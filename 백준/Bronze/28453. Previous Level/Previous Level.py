import sys
input = sys.stdin.readline

N = int(input())
level = list(map(int, input().split()))
arr = []

for i in level:
    if i == 300:
        arr.append(1)
    elif i >= 275:
        arr.append(2)
    elif i >= 250:
        arr.append(3)
    else:
        arr.append(4)

print(*arr)