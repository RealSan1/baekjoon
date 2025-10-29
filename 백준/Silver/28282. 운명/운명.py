import sys
input = lambda: sys.stdin.readline().rstrip()

X, K = map(int, input().split())
A = list(map(int, input().split()))
B = A[X:]
A = A[:X]

info = {i: [0, 0] for i in range(1, K+1)}

for num in A:
    if info[num][1] != 0:
        info[num][1] += 1
    else:
        t = X - B.count(num)
        info[num] = [t, 1]

res = 0
for key, value in info.items():
    K, Y = value[0], value[1]
    res += K * Y

print(res)