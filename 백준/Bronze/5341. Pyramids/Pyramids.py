while True:
    var = int(input())
    temp = 0
    if var == 0:
        break
    for i in range(var+1):
        temp += i
    print(temp)