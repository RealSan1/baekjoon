import sys
input = sys.stdin.readline

T = 1000000
prime = [True] * T
prime[0], prime[1] = False, False
for i in range(2, int(T ** 0.5)+1):
    if prime[i]:
        for j in range(i*i, T, i):
            prime[j] = False

A = []
for i in range(len(prime)):
    if prime[i]:
        A.append(i)

N = int(input())-1
print(A[N])