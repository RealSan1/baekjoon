import sys, itertools
input = sys.stdin.readline

prime = [True] * 3001
prime[0], prime[1] = False, False
for i in range(2, int(3001 * 0.5)+1):
    for j in range(i*i, 3001, i):
        if prime[j]:
            prime[j] = False

primes = []
for i in range(len(prime)):
    if prime[i]:
        primes.append(i)

N, M = map(int, input().split())
H = list(map(int, input().split()))
temp = list(itertools.permutations(H, M))

arr = []
for i in temp:
    if sum(i) not in arr:
        if sum(i) in primes:
            arr.append(sum(i))
arr.sort()

if len(arr) != 0:
    print(*arr)
else:
    print(-1)