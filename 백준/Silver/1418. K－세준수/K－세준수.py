import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
junsu = 0

prime = [0] * (N+1)

for i in range(2, N+1):
    if prime[i] == 0:
        for j in range(i, N+1, i):
            prime[j] = i

for i in range(1, N+1):
    if prime[i] <= K:
        junsu +=1

print(junsu)
