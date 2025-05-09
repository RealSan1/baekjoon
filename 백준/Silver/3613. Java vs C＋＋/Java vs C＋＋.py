import sys
input = sys.stdin.readline

N = input().strip()

arr = []
result = ''
Bool = False
V = False # 에러 판단


if N.count('_') > 0:
    A = N.index('_')

    if N.endswith('_'):
        V = True
        
    elif N.startswith('_'):
        V = True
    
    for a, i in enumerate(N):
        if i == '_' and A != a:
            if a - A == 1:
                V = True
                break

        if i.isupper():
            V = True
            break

        if i == '_':
            Bool = True
            continue

        if Bool:
            result += i.upper()
            Bool = False

        else:
            result += i
else:
    if N[0].isupper():
        V = True
        
    for i in N:
        if i.isupper():
            result += '_'
            result += i.lower()

        else:
            result += i

if V:
    print('Error!')
else:
    print(result)