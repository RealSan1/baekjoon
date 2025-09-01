import sys
input = lambda: sys.stdin.readline().rstrip()

P = 1000001
prime = [True] * P
prime[0], prime[1] = False, False

for i in range(2, int(P ** 0.5)+1):
    if prime[i]:
        for j in range(i*i, P, i):
            prime[j] = False

arr = []
for i in range(P):
    if prime[i]:
        arr.append(i)

res = []
primes = [True] * P
primes[0], primes[1] = False, False

for i in range(2, 30001):
    if primes[i]:
        for j in range(i*i, P, i):
            primes[j] = False

    if primes[i]:
        res.append(arr[i-1])

T = int(input())
for i in range(T):
    N = int(input())
    print(res[N-1])