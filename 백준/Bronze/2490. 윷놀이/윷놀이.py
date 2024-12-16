for i in range(3):
    N = list(input().split())
    if N.count('0') == 1:
        print('A')
    elif N.count('0') == 2:
        print('B')
    elif N.count('0') == 3:
        print('C')
    elif N.count('0') == 4:
        print('D')
    elif N.count('1') == 4:
        print('E')