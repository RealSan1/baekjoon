import sys
input = sys.stdin.readline

def solution(n):
    x = 2
    count = []
    
    while x * x <= n:
        if n % x != 0:
            x += 1
        else:
            count.append(x)
            n //= x
    if n > 1:
        count.append(n)
    return len(count)

T = 100001
prime = [True] * T
prime[0], prime[1] = False, False
for i in range(2, int(T ** 0.5)):
    if prime[i]:
        for j in range(i*i, T, i):
            prime[j] = False

primes = []
for i in range(T):
    if prime[i] :
        primes.append(i)

A, B = map(int, input().split())
result = 0
for i in range(A, B+1):
    if solution(i) in primes:
        result += 1

print(result)