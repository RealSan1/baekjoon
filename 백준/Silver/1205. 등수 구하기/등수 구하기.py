import sys
input = sys.stdin.readline

N, T, P = map(int, input().split())
if N > 0 :
    arr = list(map(int, input().split()))
else:
    arr = []

rank = [0 for i in range(P)]
arr.sort(reverse=True)

if N == P and T <= arr[-1]:
    print(-1)
else:
    for i in range(len(arr)):
        rank[i] = arr[i]

    for i in range(P):
        if T >= rank[i]:
            rank[i+1:P] = rank[i:P-1]
            rank[i] = T
            break
    
    for i in rank:
        if i == T:
            print(rank.index(i)+1)
            break
