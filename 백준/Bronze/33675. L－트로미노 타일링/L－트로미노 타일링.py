import sys
input = lambda: sys.stdin.readline().rstrip()

for i in range(int(input())):
    N = int(input())
    if N % 2 == 0:
        print(2** (N//2))
    else:
        print(0)