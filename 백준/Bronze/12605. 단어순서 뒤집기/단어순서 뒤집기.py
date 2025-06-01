import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    L = list(input().split())
    result = ' '.join(L[::-1])
    print(f'Case #{i+1}: {result}')
