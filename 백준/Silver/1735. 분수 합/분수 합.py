from fractions import Fraction
var = 0
for i in range(2):
    N, M = map(int, input().split())
    var += Fraction(N, M)

print(var.numerator, var.denominator)