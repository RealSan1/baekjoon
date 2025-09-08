import sys
import itertools
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
V = Counter(arr)

if N == 1:
    print("YES")
    exit()

for P in itertools.combinations(arr, N):
    valid = True
    for i in range(2, N):
        if P[i] != P[i-1] + P[i-2]:
            valid = False
            break
    if valid:
        if Counter(P) == V:
            print("YES")
            exit()

print("NO")