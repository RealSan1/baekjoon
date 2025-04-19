import sys
input = sys.stdin.readline

S = input().strip()
result = ['pi', 'ka', 'chu']

A = ''
for i in S:
    A += i
    if A in result:
        A = ''

if A == '':
    print("YES")
else:
    print("NO")