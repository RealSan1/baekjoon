import sys
input=sys.stdin.readline

def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

N = int(input())
for _ in range(N):
    A = int(input())
    while True:
        if A == 0 or A == 1:
            print(2)
            break

        if prime(A):
            print(A)
            break

        else:
            A += 1