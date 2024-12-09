while True:
    N = input()
    arr = []
    status = 1

    if N in '.':
        break

    for i in N:
        if i == '[' or i == '(':
            arr.append(i)

        elif i == ']':
            if len(arr) != 0 and arr[-1] == '[':
                arr.pop()
            else:
                status = 0
                break
        
        elif i == ')':
            if len(arr) != 0 and arr[-1] == '(':
                arr.pop()
            else:
                status = 0
                break
    
    if len(arr) == 0 and status == 1:
        print('yes')
    
    else:
        print('no')

