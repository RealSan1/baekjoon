import sys, itertools
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
arr = {}
for i in range(1, 2000000):
    arr[i] = False

for i in range(1, N+1):
    for j in itertools.combinations(S, i):
        num = sum(j)
        if num in arr:
            arr[num] = True
            
for i,j in arr.items():
    if not j:
        print(i)
        break