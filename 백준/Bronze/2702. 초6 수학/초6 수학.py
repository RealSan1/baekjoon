import sys, math
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    print(math.lcm(A, B), math.gcd(A, B))