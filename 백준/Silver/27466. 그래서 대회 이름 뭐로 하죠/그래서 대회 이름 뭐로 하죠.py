import sys, itertools
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
T = input()
T = sorted(T, reverse=True)
V = ['A', 'E', 'I', 'O', 'U']
if T.count('A') < 2:
    print('NO')
else:
    for i in itertools.permutations(T, M):
        i = ''.join(i)
        if i[-2] == 'A' and i[-3] == 'A' and i[-1] not in V:
            print(i)
            break