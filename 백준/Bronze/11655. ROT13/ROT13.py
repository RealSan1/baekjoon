import sys

Alpha = []
for i in range(13):
    A = chr(65+i)
    B = chr(97+i)
    Alpha.append(A)
    Alpha.append(B)

Beta = []
for i in range(13):
    A = chr(78+i)
    B = chr(110+i)
    Beta.append(A)
    Beta.append(B)

var = input()
result = ''
for i in var:
    if i in Alpha:
        T = Alpha.index(i)
        result += Beta[T]
    elif i in Beta:
        T = Beta.index(i)
        result += Alpha[T]
    else:
        result += i

print(result)