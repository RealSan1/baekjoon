import sys, math
input = lambda: sys.stdin.readline().rstrip()

S = input()
T = input()

Slen = len(S)
Tlen = len(T)

num = math.lcm(Slen, Tlen)

Slen = num//Slen
Tlen = num//Tlen

if S * Slen == T * Tlen:
    print(1)
else:
    print(0)