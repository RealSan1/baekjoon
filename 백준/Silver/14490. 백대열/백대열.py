import math
N, M = map(int, input().split(':'))
i = 2
result = math.gcd(N, M)

print(f"{N//result}:{M//result}")