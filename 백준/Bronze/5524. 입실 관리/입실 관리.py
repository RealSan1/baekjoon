import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    name = input().strip()
    print(name.lower())