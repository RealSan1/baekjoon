import sys
input = sys.stdin.readline

N = str(input())
F = int(input())
N = N[:-3]
num = '00'
while True:
    res = N + num
    if int(res) % F == 0:
        break
    
    num = int(num)
    num += 1
    num = str(num).zfill(2)

print(num)