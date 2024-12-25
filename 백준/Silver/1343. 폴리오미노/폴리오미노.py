N = input().split('.')
arr = []
for i in range(len(N)):
    if N[i] == '':
        arr.append('.')

    elif len(N[i]) == 2:
        arr.append('BB')
        arr.append('.')

    elif len(N[i]) % 4 == 0: # An = 4N
        t = len(N[i]) // 4
        arr.append('AAAA' * t)
        arr.append('.')
    
    elif len(N[i]) % 4 == 2: # An = 4N + 2
        t = len(N[i]) // 4
        arr.append('AAAA' * t + 'BB')
        arr.append('.')

    else:
        arr.append('None')
        break

if arr.count('None') > 0:
    print(-1)
else:
    print(''.join(arr)[:-1])