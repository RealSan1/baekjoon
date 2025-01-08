A, LA = map(str, input().split())
A = int(A)

if LA == 'miss':
    print(0)
elif LA == 'bad':
    print(200*A)
elif LA == 'cool':
    print(400*A)
elif LA == 'great':
    print(600*A)
elif LA == 'perfect':
    print(1000*A)