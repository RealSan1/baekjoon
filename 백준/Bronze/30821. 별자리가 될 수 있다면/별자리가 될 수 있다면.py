import sys, math
input = sys.stdin.readline

N = int(input())
result = math.factorial(N) / (math.factorial(N-5) * math.factorial(5))
print(int(result))
