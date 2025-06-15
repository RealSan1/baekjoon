import sys
input = sys.stdin.readline

N = int(input())
num = 0
res = 0
arr = {}
for _ in range(N):
    D, C = map(str, input().split())
    C = int(C)
    if C in arr:
        arr[C] += 1
    else:
        arr[C] = 1

    if D == 'jinju':
        num = C

for i,j in arr.items():
    if i > num:
        res += j
print(num)
print(res)