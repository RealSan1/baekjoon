import sys
input = sys.stdin.readline

prime = [True] * 2001
prime[0], prime[1] = False, True
primes = []
for i in range(2, int(2001 ** 0.5)):
    if prime[i]:
        for j in range(i*i, 2001, i):
            prime[j] = False

for i in range(len(prime)):
    if prime[i]:
        primes.append(i)

while True:
    try:
        N, C = map(int, input().split())

        filtered = [p for p in primes if p <= N]
        length = len(filtered)

        if length % 2 == 0:
            count = C * 2
        else:
            count = C * 2 - 1

        if count >= length:
            result = filtered
        else:
            center = length // 2
            start = center - count // 2
            end = start + count
            result = filtered[start:end]

        num = ' '.join(str(x) for x in result)
        print(f"{N} {C}: {num} \n")

    except:
        break