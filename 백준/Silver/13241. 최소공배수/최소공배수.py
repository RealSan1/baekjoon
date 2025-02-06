import sys, math
input = sys.stdin.readline

A, B = map(int, input().split())
print(math.lcm(A, B))