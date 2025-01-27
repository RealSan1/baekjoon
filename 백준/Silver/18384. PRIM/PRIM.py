import sys
input = sys.stdin.readline

T = 1000001
prime = [True] * T
prime[0], prime[1] = False, False

for i in range(2, int(T ** 1/2)+1):
    if prime[i]:
        for j in range(i*i, T, i):
            prime[j] = False

Case = int(input())
for _ in range(Case):
    N = list(map(int,input().split()))
    result = 0
    for i in N:
        for t in range(i, len(prime)):
            if prime[t]:
                result += t
                break
    print(result)
