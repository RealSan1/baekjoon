import sys
input = sys.stdin.readline
C = 1000001
prime = [True] * C
prime[0], prime[1] = False, False
for i in range(2, int(C * 0.5)+1):
    for j in range(i * i , C, i):
        if prime[j]:
            prime[j] = False

T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    if N == 4:
        count = 1
    else:
        for i in range(3, N // 2 + 1, 2):
            if prime[i] and prime[N-i]:
                count += 1
    
    print(count)