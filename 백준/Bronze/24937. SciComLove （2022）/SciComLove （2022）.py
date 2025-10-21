import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = 'SciComLove'
N = N % 10
res = S[:N]
S = S[N:]
S = S + res
print(S)