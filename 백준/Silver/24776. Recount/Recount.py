import sys

input = lambda: sys.stdin.readline().rstrip()

arr = {}
while True:
    N = input()
    if N == '***':
        break

    if N in arr:
        arr[N] += 1
    else:
        arr[N] = 1

V = sorted(arr.items(), key=lambda x: -x[1])
name = V[0][0]
num = V[0][1]

for i, j in V[1:]:
    if j == num:
        print('Runoff!')
        break
    else:
        print(name)
        break