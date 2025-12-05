import sys
input = lambda: sys.stdin.readline().rstrip()

W = int(input())
arr = []
num = []
N = int(input())
for i in range(N):
    arr.append(int(input()))

res = 0
for i in arr:
    num.append(i)
    if len(num) == 5:
        num.pop(0)

    if sum(num) > W:
        break
    res += 1

print(res)