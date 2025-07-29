import sys
input = sys.stdin.readline

N = list(map(str, input().strip()))
N.sort(reverse=True)

res = 0
num = ''
for i in range(len(N)):
    res += int(N[i])

if res % 3 != 0 or N[len(N)-1] != "0":
    print(-1)
else:
    for i in range(len(N)):
        num += N[i]
    print(num)