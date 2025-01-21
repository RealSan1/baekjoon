import sys
input = sys.stdin.readline

A, B, D = map(int, input().split())
D = str(D)
result = 0
prime = [True] * (B + 1)
prime[0], prime[1] = False, False

for i in range(2, int(B**1/2)+1):
    if prime[i]:
        for j in range(i*i, B+1, i):
            prime[j] = False

for i in range(A, B+1):
    if prime[i] and D in str(i):
        result += 1

print(result)