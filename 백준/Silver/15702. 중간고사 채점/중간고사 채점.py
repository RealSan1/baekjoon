import sys
input = sys.stdin.readline
  
N, M = map(int, input().split())
arr = {}
solve = list(map(int, input().split()))
for _ in range(M):
    std = list(map(str, input().split()))
    res = 0
    for i, j in enumerate(std[1:]):
        if j == 'O':
            res += solve[i]
    
    arr[int(std[0])] = res

print(*sorted(arr.items(), key=lambda x : (-x[1], x[0]))[0])