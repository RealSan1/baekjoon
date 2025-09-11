import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(input())

seat = '0' * K
res = 0
for i in arr:
    num = ''
    for j in i:
        if j == '0':
            num += j
        else:
            num = ''
        if seat == num:
            res += 1
            num = num[1:]

print(res)