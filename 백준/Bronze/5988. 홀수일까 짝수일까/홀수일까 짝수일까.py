import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
for _ in range(N):
    K = int(input())
    if K % 2 == 0:
        print('even')
    else:
        print('odd')