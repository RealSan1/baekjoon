import math 
n, k = map(int, input().split())
n = n-1
k = k-1
result = math.factorial(n) / (math.factorial(n-k) * math.factorial(k))

print(int(result))
