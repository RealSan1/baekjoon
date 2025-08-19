import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = input()
res = ''
for i in S:
    if i == 'I':
        res += 'i'
    else:
        res += 'L'

print(res)