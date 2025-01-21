import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split()) # 상근 선영
    N_set = set()
    M_set = set()
    if N == 0 and M == 0:        
        break

    for i in range(N):
        A = int(input())
        N_set.add(A)
    
    for i in range(M):
        A = int(input())
        M_set.add(A)

    print(len(N_set & M_set))