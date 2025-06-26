import sys
input = sys.stdin.readline

N = int(input())
arr = []
cost = {'P':0, 'C':0, 'V':0, 'S':0, 'G':0, 'F':0, 'O':0}
for _ in range(N):
    G = list(input().strip())
    arr.append([list(set(G)), len(G)])

C = list(map(int, input().split()))
for i, c in enumerate(C):
    if i == 0:
        cost['P'] = c
    elif i == 1:
        cost['C'] = c
    elif i == 2:
        cost['V'] = c
    elif i == 3:
        cost['S'] = c
    elif i == 4:
        cost['G'] = c
    elif i == 5:
        cost['F'] = c
cost['O'] = int(input())

res = 0
for G, S in arr:
    if len(G) > 1: # 일반
        res += S * cost['O']
    else:
        MIN = sys.maxsize
        MIN = min(MIN, cost[G[0]] * S)
        MIN = min(MIN, cost['O'] * S)
        res += MIN

print(res)