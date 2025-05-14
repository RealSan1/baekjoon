import sys
input = sys.stdin.readline

N = int(input())
arr = {}
ocean, temperature, oxygen  = 0, -30, 0

for i in range(N):
    A, B = map(str, input().split())
    B = int(B[1:])
    if A == 'ocean':
        ocean += B
    elif A == 'temperature':
        temperature += B
    else:
        oxygen += B

if ocean >= 9 and oxygen >= 14 and temperature >= 8:
    print('liveable')
else:
    print('not liveable')