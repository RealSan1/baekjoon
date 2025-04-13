import sys, itertools
input = sys.stdin.readline

X = list(map(int, input().strip()))
temp = int(''.join(str(i) for i in X))
Bool = False
X.sort()
for i in itertools.permutations(X, len(X)):
    num = int(''.join(map(str, i)))

    if num > temp:
        Bool = True
        break

if Bool:
    print(num)
else:
    print(0)