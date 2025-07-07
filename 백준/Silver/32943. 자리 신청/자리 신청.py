import sys
input = sys.stdin.readline

X, C, K = map(int, input().split())
arr = []
ck = {}
seat = {}

for _ in range(K):
    log = list(map(int, input().split()))
    arr.append(log)

arr = sorted(arr, key=lambda x: x[0])

for t, s, n in arr:
    if s in seat:
        continue

    if n in ck:
        num = ck[n]
        del seat[num]

    ck[n] = s
    seat[s] = n

for n in sorted(ck):
    print(n, ck[n])