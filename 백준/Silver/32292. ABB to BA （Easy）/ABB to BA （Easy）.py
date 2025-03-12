import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = int(input())
    N = input().strip()
    while True:
        if 'ABB' not in N:
            break
        
        N = N.replace('ABB', 'BA')

    print(N)