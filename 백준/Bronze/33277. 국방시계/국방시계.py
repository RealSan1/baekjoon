import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = (M / N) * 24

hours = int(result)
minutes = int((result - hours) * 60)

print(f"{hours:02}:{minutes:02}")
