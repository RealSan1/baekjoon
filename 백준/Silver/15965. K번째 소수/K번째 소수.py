import sys
input = sys.stdin.readline

K = int(input())

T = K * 15
prime = [True] * T
prime[0], prime[1] = False, False
for i in range(2, int(T ** 0.5)+1):
    for j in range(i*i, T, i):
        if prime[j]:
            prime[j] = False

A = []
for i in range(len(prime)):
    if prime[i]:
        A.append(i)

count = 0
for i in range(T):
    if prime[i]:
        count += 1
        if count == K:
            print(i)
            break