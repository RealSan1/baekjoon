import sys, itertools
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    X, Y = map(int, input().split())
    arr = list(map(int, input().split()))
    Bool = False
    for i in range(1, 6):
        for n in itertools.combinations(arr, i):
            res = sum(n)
            if res >= X and res <= Y:
                Bool = True
                break
        if Bool:
            break
    
    if Bool:
        print("YES")
    else:
        print("NO")