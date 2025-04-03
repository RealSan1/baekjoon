import sys
input = sys.stdin.readline

N = []
while True:
    if N and len(N) == N[0]+1:
        break
    N.extend(list(map(int, input().split())))
del N[0]

result = [0]  * len(N)
for i in range(len(N)):
    result[i] = int(str(N[i])[::-1])

result.sort()
for i in result:
    print(i)