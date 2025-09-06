import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
s = list(input())

V = ['A', 'E', 'I', 'O', 'U']
ans = []

while s and s[-1] in V:
    s.pop()

if not s:
    print("NO")
    sys.exit()

ans.append(s.pop())

while s and s[-1] != 'A':
    s.pop()

if not s:
    print("NO")
    sys.exit()

ans.append(s.pop())

while s and s[-1] != 'A':
    s.pop()

if not s:
    print("NO")
    sys.exit()

ans.append(s.pop())

if len(s) + 3 < M:
    print("NO")
    sys.exit()

print("YES")
print("".join(s[:M-3] + ans[::-1]))
