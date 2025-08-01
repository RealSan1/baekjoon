import sys
input = sys.stdin.readline

A = list(input().strip())
B = list(input().strip())

for i in A:
    B.remove(i)

print(''.join(set(B)))