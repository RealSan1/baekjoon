prime = [True] * 10001
prime[0], prime[1] = False, True
for i in range(2, int(10001 * 0.5)+1):
    for j in range(i*i, 10001, i):
        if prime[j]:
            prime[j] = False
primes = []
for i in range(len(prime)):
    if prime[i]:
        primes.append(i)

A = input()
hap = 0
for i in A:
    if ord(i) > 96:
        hap += (ord(i) - 96)
    else:
        hap += (ord(i) - 38)
    
if hap in primes:
    print('It is a prime word.')
else:
    print('It is not a prime word.')