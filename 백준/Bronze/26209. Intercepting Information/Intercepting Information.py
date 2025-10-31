import sys
input = lambda: sys.stdin.readline().rstrip()

N = list(map(int, input().split()))

if 9 in N:
    print('F')
else:
    print('S')