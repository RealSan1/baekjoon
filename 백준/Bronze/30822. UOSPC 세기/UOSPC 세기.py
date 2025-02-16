import sys
input = sys.stdin.readline
n = int(input())
S = input()
u = S.count('u')
o = S.count('o')
s = S.count('s')
p = S.count('p')
c = S.count('c')

print(min(u, o, s, p, c))