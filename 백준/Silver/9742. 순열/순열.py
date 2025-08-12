import sys, itertools
input = lambda: sys.stdin.readline().rstrip()

while True:
    try:
        A, B = map(str, input().split())
        B = int(B)
        num = 1
        Bool = False
        for i in itertools.permutations(A, len(A)):
            if num == B:
                Bool = True
                break
            num += 1

        if Bool:
            print(f"{A} {B} = {''.join(i)}")
        else:
            print(f"{A} {B} = No permutation")
    except:
        break