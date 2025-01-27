import sys
input = sys.stdin.readline
N = int(input())
T = 10000000
prime = [True] * 10000000
prime[0], prime[1] = False, False
A = []

for i in range(2, int(10000000 ** 1/2)+1):
    if prime[i]:
        for j in range(i*i, 10000000, i):
            prime[j] = False

for i in range(N, len(prime)):
    if prime[i]:
        A.append(i)

for i in A:
    S = str(i)
    SR = str(i)[::-1]
    if S == SR:
        print(i)
        break