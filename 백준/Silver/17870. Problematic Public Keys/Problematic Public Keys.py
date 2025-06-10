import sys
input = sys.stdin.readline

M = int(input())
num = set()
def prime(K):
    i = 2
    while True:
        if K % i == 0:
            K //= i
            break
        else:
            i += 1
    
    return i, K
for _ in range(M):
    K = int(input())
    A, B = prime(K)
    num.add(A)
    num.add(B)

for idx, i in enumerate(sorted(num), 1):
    print(i, end=' ')
    if idx % 5 == 0:
        print() 