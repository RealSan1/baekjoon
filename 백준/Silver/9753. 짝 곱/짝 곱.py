import sys
input = sys.stdin.readline
C = 100001
prime = [True] * C
prime[0], prime[1] = False, False
for i in range(2, int(C * 0.5)+1):
    for j in range(i * i , C, i):
        if prime[j]:
            prime[j] = False

A = []
for i in range(len(prime)):
    if prime[i]:
        A.append(i)

T = int(input())
for _ in range(T):
    N = int(input())
    small = sys.maxsize
    for i in A:
        for j in A:
            if i * j >= N and i != j:
                if i * j > small:
                    break
                small = min(small, i*j)
    
    print(small)
