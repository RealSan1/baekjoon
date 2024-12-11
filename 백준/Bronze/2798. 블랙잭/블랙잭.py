N, M = map(int, input().split())
T = list(map(int, input().split()))
T.sort(reverse=True)
arr = []
for i in range(N):
    for j in range(1, N):
        for t in range(2, N):
            var = T[i]+T[j]+T[t]
            if var <= M and T[i] != T[j] and T[i] != T[t] and T[j] != T[t]:
                arr.append(var)

print(max(arr))

