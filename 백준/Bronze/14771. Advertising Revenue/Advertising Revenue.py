import sys
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
for k in range(K):
    cost = 0
    N, V = map(int, input().split())
    arr = []
    for n in range(N):
        D, P = map(int, input().split())
        arr.append([D, P])
    for v in range(V):
        A1, A2, C = map(int, input().split())
        ad1, ad2 = arr[A1-1], arr[A2-1]
        if 1 == ad1[0]: 
            cost += ad1[1]
        
        if 1 == ad2[0]:
            cost += ad2[1]

        if C == 1 and ad1[0] == 0: # A1 Click
            cost += ad1[1]
        
        if C == 2 and ad2[0] == 0: # A2 Click
            cost += ad2[1]

    print(f"Data Set {k+1}:")
    print(cost)
    print()