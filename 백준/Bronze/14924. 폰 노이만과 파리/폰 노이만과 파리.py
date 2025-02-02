import sys
input = sys.stdin.readline

S, T, D = map(int, input().split())

cal = D/(S*2)
print(int(T*cal))
