T = int(input())
arr = []
for i in range(T):
    N = input().split(' ')
    for W in N:
        arr.append(W[::-1])
    print(*arr)
    arr = []