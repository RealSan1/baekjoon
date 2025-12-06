import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
B.sort()

print(A[-1] + B[-1])