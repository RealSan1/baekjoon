import sys
input = sys.stdin.readline

arr = [i for i in range(1, 10001)]
for i in range(1, 10001):
    num = 0
    for j in range(1, i):
        if i % j == 0:
            num += 1
        
    if num % 2 == 1:
        arr.remove(i)

M = int(input())
N = int(input())
res = []
for i in arr:
    if N >= i and M <= i:
        res.append(i)

if len(res) > 0:
    print(sum(res))
    print(res[0])
else:
    print(-1)