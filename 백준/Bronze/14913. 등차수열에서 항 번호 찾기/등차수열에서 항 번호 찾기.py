A, D, K = map(int, input().split())
var = 0
for i in range(1000000):
    An = A + D*i
    var +=1
    if K == An:
        print(var)
        break
    elif i == 999999 and K != An:
        print('X')