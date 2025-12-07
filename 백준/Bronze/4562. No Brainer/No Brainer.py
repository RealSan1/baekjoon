import sys
input = lambda: sys.stdin.readline().rstrip()

for i in range(int(input())):
    A, B = map(str, input().split())
    if A >= B:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")