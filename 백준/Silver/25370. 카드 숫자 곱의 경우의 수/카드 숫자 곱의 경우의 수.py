import sys, itertools
input = sys.stdin.readline

def solve(V):
    ans = 1
    for i in V:
        ans *= i
    return ans

N = int(input())
card = [i for i in range(1, 10)]
result = set()
for i in itertools.combinations_with_replacement(card, N):
    result.add(solve(i))

print(len(result))