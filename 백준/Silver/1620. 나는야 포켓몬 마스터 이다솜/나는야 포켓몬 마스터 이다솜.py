import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = [] # 문제
dex_num = {}
dex_name = {}
for i in range(N): # 도감 입력
    pokemon = sys.stdin.readline().strip('\n')
    dex_name[pokemon] = i+1
    dex_num[i+1] = pokemon

for i in range(M): # 문제
    solve = sys.stdin.readline().strip('\n')
    if solve.isdigit(): # 정수 입력 (도감번호)
        solve = int(solve)
        arr.append(dex_num[solve])
    else: # 문자 입력
        arr.append(dex_name[solve])

for i in range(len(arr)):
    print(arr[i])