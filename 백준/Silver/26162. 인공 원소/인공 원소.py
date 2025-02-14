import sys
input = sys.stdin.readline

primes = [True] * 119
primes[0], primes[1] = False, False
for i in range(2, int(119 * 0.5)+1):
    for j in range(i*i, 119, i):
        if primes[j]:
            primes[j] = False
prime = []
for i in range(len(primes)):
    if primes[i]:
        prime.append(i)

N = int(input())
for _ in range(N):
    a = int(input())
    for i in prime:
        Bool = False
        for j in prime:
            if i+j == a:
                print('Yes')
                Bool = True
                break
        if Bool:
            break
    else:
        print('No')
