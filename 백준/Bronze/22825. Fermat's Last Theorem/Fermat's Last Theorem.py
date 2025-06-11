import sys
input = sys.stdin.readline

while True:
    Z = int(input())
    if Z == 0:
        break
    count = 0
    for i in range(1, Z+1):
        for j in range(1, Z+1):
            if Z ** 3 >= i ** 3 + j ** 3:
                count = max(count, i**3 + j**3)

    print(Z ** 3 - count)