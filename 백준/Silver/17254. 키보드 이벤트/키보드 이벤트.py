import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = []
for _ in range(M):
    A, B, C = map(str, input().split())
    A, B = int(A), int(B)
    arr.append([A, B, C])
    
res = ''
for i in sorted(arr, key=lambda x: (x[1], x[0])):
    res += i[2]

print(res)
