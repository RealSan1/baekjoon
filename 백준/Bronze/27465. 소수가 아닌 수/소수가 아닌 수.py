import sys
input = sys.stdin.readline

T = 1000001
prime = [True] * T
prime[0], prime[1] = False, False

for i in range(2, int(T ** 0.5)+1):
    for j in range(i*i, T, i):
        if prime[j]:
            prime[j] = False

A = []
for i in range(len(prime)):
    if not prime[i]:
        A.append(i)

N = int(input())

for i in A:
    if i > N:
        print(i)
        break
