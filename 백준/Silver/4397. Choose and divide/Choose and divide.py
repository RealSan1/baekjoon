import sys, math
from decimal import Decimal
input = lambda: sys.stdin.readline().rstrip()

while True:
    line = input().split()
    if not line:
        break
    P, Q, R, S = map(int, line)
    num = Decimal(str(math.factorial(P) / Decimal(math.factorial(Q) * math.factorial(P-Q))))
    num1 = Decimal(str(math.factorial(R) / Decimal(math.factorial(S) * math.factorial(R-S))))
    res = num / num1
    print(f"{res:.5f}")
