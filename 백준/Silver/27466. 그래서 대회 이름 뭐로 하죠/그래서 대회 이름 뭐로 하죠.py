import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
S = input()

V = ['A', 'E', 'I', 'O', 'U']
arr = []

for i in range(N-1, 0, -1):
    if len(arr) == 0 and S[i] not in V:
        arr.append(S[i])
    elif (len(arr) == 1 or len(arr) == 2) and S[i] == 'A':
        arr.append(S[i])
    elif len(arr) >= 3:
        arr.append(S[i])

    if len(arr) == M:
        break

if len(arr) != M:
    print('NO')
else:
    print(''.join(arr[::-1]))