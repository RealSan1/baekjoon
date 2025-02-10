import sys
from decimal import Decimal, getcontext

getcontext().prec = 1000010 
input = sys.stdin.readline

A, B, N = map(int, input().split())
R1 = Decimal(A) / Decimal(B)

decimal_part = str(R1 % 1)[2:] 

if N <= len(decimal_part):
    print(decimal_part[N - 1])
else:
    print(0)
