import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(num):
    lst = []
    for i in range(num, 1, -1):
        if num % i == 0:
            lst.append(num//i)
    lst.append(num)
    return lst

P, Q = map(int, input().split())
A = solve(P)
B = solve(Q)

for i in A:
    for j in B:
        print(i, j)