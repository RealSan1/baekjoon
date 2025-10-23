import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = input()
while True:
    if S.count('s') == S.count('t'):
        break
    S = S[1:]

print(S)