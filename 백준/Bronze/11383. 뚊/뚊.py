import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
Bool = True
arr = []
for _ in range(N):
    num = input()
    res = ''
    for i in num:
        res += i*2
    arr.append(res)

for i in arr:
    res = input()
    if i != res:
        Bool = False

if Bool:
    print("Eyfa")
else:
    print("Not Eyfa")
