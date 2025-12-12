import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = input()
M = int(input())
S = input()

num = Z = 0
Bool = False
while True:
    if arr[(num + N - 1) % N] == S[Z] and num != 0:
        Z += 1
    
    if Z == len(S):
        Bool = True
        break

    if num > 10000:
        break

    num += 1

if Bool:
    print(num)
else:
    print(-1)