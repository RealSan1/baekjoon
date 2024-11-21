import math

A, B = map(int, input().split(' '))

for i in range(A, B + 1):
    if i == 1:
        continue
    a = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            a = False
            break
    if a:
        print(i)