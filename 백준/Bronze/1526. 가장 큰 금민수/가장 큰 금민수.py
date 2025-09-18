import sys
input = lambda: sys.stdin.readline().rstrip()

def check(num):
    return str(num).count('4') + str(num).count('7')
N = int(input())
up = N
down = N
for i in range(1000001):
    if check(down) == len(str(down)): 
        print(down)
        break

    down -= 1