import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = []
for n in range(N):
    sol = list(map(int, input().split()))
    Bool = True
    for i, j in enumerate(sol):
        i = (i % 5) + 1
        res = ((j - 1) % 5) + 1
        if res != i:
            Bool = False
            break
    
    if Bool:
        arr.append(n+1)

for i in arr:
    print(i)