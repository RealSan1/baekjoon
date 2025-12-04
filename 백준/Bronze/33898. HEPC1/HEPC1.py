import sys
input = lambda: sys.stdin.readline().rstrip()

A = input()
B = input()
HEPC = 'HEPC'
V = False
res = A+B[::-1]
for i in range(4):
    num = ''
    for j in range(4):
        num += res[(i + j) % 4]
    if HEPC == num:
        V = True

res = A[0] + B+ A[1]
for i in range(4):
    num = ''
    for j in range(4):
        num += res[(i + j) % 4]
    if HEPC == num:
        V = True

if V:
    print('YES')
else:
    print('NO')