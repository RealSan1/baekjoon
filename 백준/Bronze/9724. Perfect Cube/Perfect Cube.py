import sys,math
input = lambda: sys.stdin.readline().rstrip()

for i in range(int(input())):
    A, B = map(int, input().split())

    print(f"Case #{i+1}: {math.floor(int(B**(1/3)) - math.ceil(A**(1/3))) + 1}")
