from fractions import Fraction

N = int(input())
arr = list(map(int, input().split()))

for i in range(1, len(arr)):
    f = Fraction(arr[0], arr[i])
    if f.denominator == 1 :
        print(f"{f.numerator}/1")
    else:
        print(f"{f.numerator}/{f.denominator}")