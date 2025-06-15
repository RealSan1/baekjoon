import sys
input = sys.stdin.readline

N = int(input())
num = 0
res = 0
arr = {i: 0 for i in range(1002)}
for _ in range(N):
    D, C = map(str, input().split())
    C = int(C)
    if C > 1001:
        C = 1001

    if C in arr:
        arr[C] += 1

    if D == 'jinju':
        num = C

for i,j in arr.items():
    if i > num:
        res += j

print(num)
print(res)