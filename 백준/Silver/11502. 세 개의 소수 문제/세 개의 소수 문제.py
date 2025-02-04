import sys
import itertools
input = sys.stdin.readline

T = 1001
prime = [True] * T
prime[0], prime[1] = False, False
for i in range(2, int(T**0.5)+1):
    for j in range(i*i, T, i):
        if prime[j]:
            prime[j] = False

arr = []
for i in range(len(prime)):
    if prime[i]:
        arr.append(i)


T = int(input())
for _ in range(T):
    K = int(input())
    Bool = False
    for x in arr:
        for y in arr:
            for z in arr:
                if x+y+z == K:
                    print(x, y, z)
                    Bool = True
                    break
            if Bool:
                break
        if Bool:
                break