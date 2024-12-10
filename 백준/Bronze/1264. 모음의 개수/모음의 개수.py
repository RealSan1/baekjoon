while True:
    N = input()
    if N == '#':
        break
    N = N.lower()
    var = N.count('a') + N.count('e') + N.count('i') + N.count('o') + N.count('u')
    print(var)