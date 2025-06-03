import sys, itertools
input = sys.stdin.readline

L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
moum = ['a', 'e', 'i', 'o', 'u']
result = set()
for i in itertools.combinations(arr, L):
    V = ''.join(i)
    if sum(1 for ch in V if ch in moum and ch.isalpha()) >= 1: # 모음
        if sum(1 for ch in V if ch.isalpha() and ch not in moum) >= 2: # 자음
            result.add(V)
                
for i in sorted(result):
    print(i)
