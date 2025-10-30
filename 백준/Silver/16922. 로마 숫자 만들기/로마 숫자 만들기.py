import sys, itertools
input = lambda: sys.stdin.readline().rstrip()

roma = [1, 5, 10, 50]

N = int(input())

res = set()
for i in itertools.combinations_with_replacement(roma, N):
    res.add(sum(i))

print(len(res))