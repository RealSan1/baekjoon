import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ban = []
le = {'0' : 'O', '1' : 'L', '2' : 'Z', '3': 'E', '5' : 'S',
      '6' : 'B', '7' : 'T', '8' : 'B'}
for _ in range(N):
    ban.append(input().strip())

for _ in range(M):
    num = input().strip()
    res = ''
    for i in num:
        if i in le:
            res += le[i]
        else:
            res += i
    
    A = len(res)
    Bool = False
    for i in ban:
        res = res.replace(i, '')
        if len(res) != A:
            Bool = True
            break
    if Bool:
        print("INVALID")
    else:
        print("VALID")