import sys, itertools
input = lambda: sys.stdin.readline().rstrip()

V = input()
N = int(input())
arr = {}
for _ in range(N):
    A = input()
    if A.count(','):
        A = A.split(',')
        num = []
        for i in A:
            num.append(i)
        Z = num[0][0]
        num[0] = num[0][2:]
        arr[Z] = num

    else:
        num = A[2:]
        Z = A[0]
        arr[Z] = [num]

keys = sorted(arr.keys())
results = []
for i in itertools.product(*[arr[k] for k in keys]):
    res = V
    for k, v in zip(keys, i):
        res = res.replace(k, v)
    results.append(res)

for r in sorted(results):
    print(r)