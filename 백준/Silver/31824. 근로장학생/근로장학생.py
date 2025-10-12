import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = {}
for _ in range(N):
    Q, A = map(str, input().split())
    arr[Q] = A
    
arr = sorted(arr.items(), key=lambda x: (x[0]))

for _ in range(M):
    S = input()
    res = ''
    for k in range(len(S)):
        for i, j in arr:
            if S.startswith(i, k):
                res += j
    if res:
        print(res)
    else:
        print(-1)