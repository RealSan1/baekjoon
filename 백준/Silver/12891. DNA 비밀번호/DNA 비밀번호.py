import sys
input = lambda: sys.stdin.readline().rstrip()

S, P = map(int, input().split())
DNA = input()
ACGT = list(map(int, input().split()))

vs = [0, 0, 0, 0]
res = 0

def idx(c):
    if c == 'A': return 0
    if c == 'C': return 1
    if c == 'G': return 2
    return 3

for i in range(P):
    vs[idx(DNA[i])] += 1

for j in range(4):
    if ACGT[j] > vs[j]: 
        break
    if j == 3: 
        res += 1

for i in range(P, S):
    vs[idx(DNA[i - P])] -= 1
    vs[idx(DNA[i])] += 1

    for j in range(4):
        if ACGT[j] > vs[j]: 
            break
        if j == 3: 
            res += 1

print(res)