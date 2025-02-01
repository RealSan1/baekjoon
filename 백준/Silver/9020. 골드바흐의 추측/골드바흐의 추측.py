import sys
input = sys.stdin.readline

V = 10008
prime = [True] * V
prime[0], prime[1] = False, False
for i in range(2,int(V ** 0.5) + 1):
    for j in range(i*i, V, i):
        if prime[j]:
            prime[j] = False

A = []
for i in range(len(prime)):
    if prime[i]:
        A.append(i)

T = int(input())
for _ in range(T):
    N = int(input())

    prime_1 = N // 2
    prime_2 = N // 2
    while True:
        if prime_1 in A and prime_2 in A:
            print(prime_1, prime_2)
            break
        else:
            prime_1 -= 1
            prime_2 += 1