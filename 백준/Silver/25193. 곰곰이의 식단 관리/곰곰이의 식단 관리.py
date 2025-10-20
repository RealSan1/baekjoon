import sys, math
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = input()

c = S.count('C')
r = N - c

if r == 0:
    print(c)
else:
    print(math.ceil(c / (r + 1)))
