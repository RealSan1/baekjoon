P = int(input())
for _ in range(P):
    A = list(map(int, input().split()))
    A = A[1:]
    count = 0
    for i in range(1, 20):
        for j in range(i):
            if A[j] > A[i]:
                count +=1
                A[j], A[i] = A[i], A[j]
    print(_+1, count)