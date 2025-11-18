import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

def solve(n):
    num = 4 * n
    for i in range(num):
        print('@' * n)
    
    for i in range(n):
        print('@@@@@' * n)

solve(N)