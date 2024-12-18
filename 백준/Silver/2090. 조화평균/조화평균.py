from fractions import Fraction

N = int(input())
L = list(map(int, input().split()))
temp = 0
if len(L) != 1:
    for i in range(N):
        temp += Fraction(1, L[i])
    print(1/temp)
else:
    print(f"{L[0]}/{1}")