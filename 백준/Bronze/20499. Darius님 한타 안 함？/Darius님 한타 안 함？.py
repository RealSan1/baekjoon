import sys
input = lambda: sys.stdin.readline().rstrip()

K, D, A = map(int, input().split('/'))
if K + A < D or D == 0:
    print('hasu')
else:
    print('gosu')