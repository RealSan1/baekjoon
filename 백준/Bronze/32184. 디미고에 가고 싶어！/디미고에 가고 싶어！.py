import sys, math
input = lambda: sys.stdin.readline().rstrip()

A, B = map(int, input().split())

if A % 2 == 0:
    num = 1
else:
    num = 0.5
for i in range(A, B+1):
    num += 0.5

print(math.floor(num))