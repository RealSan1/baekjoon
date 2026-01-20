import sys
input = lambda: sys.stdin.readline().rstrip()

A = input()
B = list(map(str, input().split()))
res = ''

for i in A:
    if i.upper() in B:
        res += i.lower()
    else:
        res += i

print(res)