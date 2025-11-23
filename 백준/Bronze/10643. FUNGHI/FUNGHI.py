import sys
input = lambda: sys.stdin.readline().rstrip()

arr = []
for _ in range(8):
    arr.append(int(input()))

res = 0
for i in range(8):
    num = 0
    for j in range(4):
        num += arr[(i+j) % 8]
    res = max(num, res)

print(res)