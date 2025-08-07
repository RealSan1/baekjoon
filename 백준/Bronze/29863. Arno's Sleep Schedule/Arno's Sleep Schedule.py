import sys
input = lambda: sys.stdin.readline().rstrip()

A = int(input())
B = int(input())

if A >= 20 and A <= 23:
    res = 24
    res -= A
    res += B

elif A >= 0 and A <= 3:
    res = B - A

print(res)