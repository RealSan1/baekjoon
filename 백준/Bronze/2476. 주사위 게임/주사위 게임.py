import sys
input = sys.stdin.readline

T = int(input())
result = 0
for _ in range(T):
    A, B, C = map(int, input().split())
    if A!=B and B!=C and C!=A:
        hap= max(A,B,C) * 100

    elif A == B and B == C:
        hap = 10000 + A * 1000

    elif A == B and B != C:
        hap = 1000 + A * 100

    elif A == C and A != B:
        hap = 1000 + A * 100

    elif B == C and A != B:
        hap = 1000 + B * 100
    
    result = max(result, hap)

print(result)