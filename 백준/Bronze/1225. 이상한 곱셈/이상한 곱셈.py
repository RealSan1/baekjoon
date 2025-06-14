import sys
input = sys.stdin.readline

A, B = map(str, input().split())
num = 0
for i in A:
    for j in B:
        num += int(i) * int(j)

print(num)