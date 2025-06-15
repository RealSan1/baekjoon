import sys
from functools import lru_cache
input = sys.stdin.readline

@lru_cache(maxsize=None)
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def dfs(num, length, N, result):
    if length == N:
        result.append(num)
        return
    
    for i in range(1, 10):  
        next_num = num * 10 + i
        if prime(next_num):
            dfs(next_num, length + 1, N, result)

N = int(input())
result = []

for i in [2, 3, 5, 7]:
    dfs(i, 1, N, result)

for num in result:
    print(num)