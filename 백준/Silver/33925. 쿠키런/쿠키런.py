import sys
input = sys.stdin.readline

N, J, S, H, K = map(int, input().split())

size = [input().strip() for _ in range(3)]
result = []
for i in range(1, N):
   arr = size[0][i] + size[1][i] + size[2][i]
   if arr != '...':
    result.append(arr)
    
result.sort() # 가능한 1단먼저

for i in result:
    if i == '..^': # 1단
        if J < 1:
            H -= K
        else:
            J -= 1
    elif i == '.^^': # 2단
        if J < 2:
            H -= K
        else:
            J -= 2
    elif i == 'vv.': # 슬라
        if S < 1:
            H -= K
        else:
            S -= 1

    if H < 0:
        break

if H > 0:
   print(H)
else:
   print(-1)