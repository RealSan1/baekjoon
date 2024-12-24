for _ in range(3):
    case = int(input())
    result = 0
    for i in range(case):        
        num = int(input())
        result += num
    if result > 0:
        print("+")
    elif result < 0:
        print("-")
    elif result == 0:
        print(0)

