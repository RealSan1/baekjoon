import sys
input = lambda: sys.stdin.readline().rstrip()

T = 10000001
prime = [True] * T
prime[0], prime[1] = False, False
primes = []
for i in range(2, int(T ** 0.5)):
    if prime[i]:
        for j in range(i*i, T, i):
            prime[j] = False

T = int(input())
for i in range(T):
    N = int(input())
    if prime[N+1]:
        print(1)
        print(1, N+1)
    else:
        print(0)
