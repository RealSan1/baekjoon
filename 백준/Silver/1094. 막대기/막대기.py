X = int(input())
S = 64
temp = 64
i = 1
if X == 64:
    print(1)
else:
    while True:
        temp //= 2
        S -= temp
        if S < X:
            i+=1
            S += temp

        elif S == X:
            break


    print(i)

        