N = int(input())
T = [0] * 36
T[0] = 1
T[1] = 1
T[2] = 2

for i in range(3, N+1):
    for j in range(i):
        T[i] += T[j] * T[i-1-j]

print(T[N])