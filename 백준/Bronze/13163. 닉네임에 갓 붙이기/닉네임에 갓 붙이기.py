import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = list(map(str, input().split()))
    N[0] = 'god'
    print(''.join(N))