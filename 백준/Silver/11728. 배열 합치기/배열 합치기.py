A, B = map(int, input().split())
N = list(map(int, input().split()))
M = list(map(int, input().split()))

result = N + M
print(*list(sorted(result)))