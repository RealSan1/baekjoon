import sys
input = sys.stdin.readline

N = int(input())
num = 0
res = 0
arr = []
for _ in range(N):
    D, C = map(str, input().split())
    if num != 0:
        if int(C) > num:
            res += 1
    else:
        arr.append(int(C))
        
    if D == 'jinju':
        num = int(C)

for i in arr:
    if i > num:
        res += 1

print(num)
print(res)