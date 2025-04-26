import sys, itertools
input = sys.stdin.readline

V = 9999999
prime = [True] * V
prime[0], prime[1] = False, False
for i in range(2, int(V * 0.5)+1):
    if prime[i]:
        for j in range(i*i, V, i):
            prime[j] = False

C = int(input())
for c in range(C):
    N = list(map(int, input().strip()))
    result = set()
    for A in range(len(N), 0, -1):
        for i in itertools.permutations(N, A):
            result.add(int(''.join(str(x) for x in i)))
    try:
        count = 0
        for i in result:
            if prime[i]:
                count += 1
        print(count)
    except:
        print(0)