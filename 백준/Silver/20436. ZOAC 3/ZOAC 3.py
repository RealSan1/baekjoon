import sys
input = lambda: sys.stdin.readline().rstrip()

Lloca = {'z': [0, 0], 'x': [0, 1], 'c': [0, 2], 'v': [0, 3], 
        'a': [1, 0], 's': [1, 1], 'd': [1, 2], 'f': [1, 3], 'g': [1, 4], 
        'q': [2, 0], 'w': [2, 1], 'e': [2, 2], 'r': [2, 3], 't': [2, 4]}

Rloca = {'b': [0, 4], 'n': [0, 5], 'm': [0, 6],
         'h': [1, 5], 'j': [1, 6], 'k': [1, 7], 'l': [1, 8],
         'y': [2, 5], 'u': [2, 6], 'i': [2, 7], 'o': [2, 8], 'p': [2, 9]}

L, R = map(str, input().split())
L = Lloca[L]
R = Rloca[R]
word = input()
time = 0
for i in word:
    if i in Lloca:
        x, y = Lloca[i]
        time += abs(L[0] - x) + abs(L[1] - y)   
        L = [x, y]
    else:
        x, y = Rloca[i]
        time += abs(R[0] - x) + abs(R[1] - y)
        R = [x, y]

    time += 1

print(time)