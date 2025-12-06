import sys
input = lambda: sys.stdin.readline().rstrip()

for i in range(int(input())):
    A, B = map(str, input().split())
    if sorted(A) == sorted(B):
        print('Possible')
    else:
        print('Impossible')