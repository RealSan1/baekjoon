import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    input()
    N, M = map(int, input().split())
    A = set(map(str, input().split()))
    B = set(map(str, input().split()))

    print(len(A)+ len(B) - len(A & B))