import sys
input = lambda: sys.stdin.readline().rstrip()

N = input()
res = 1

for i in range(len(N)):
    if i == 0:
        if N[i] == 'c':
            res *= 26
        else:
            res *= 10
    else:
        if N[i] == N[i - 1]:
            if N[i] == 'c':
                res *= 25 
            else:
                res *= 9
        else:
            if N[i] == 'c':
                res *= 26 
            else:
                res *= 10
    res %= 1000000009

print(res)