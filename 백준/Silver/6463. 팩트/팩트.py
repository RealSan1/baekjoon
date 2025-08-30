import sys
input = lambda: sys.stdin.readline().rstrip()

arr = []
while True:
    try:
        N = int(input())
        num = 1
        for i in range(1, N+1):
            num *= i
            num %= 100000000
            while num > 10 and num % 10 == 0:
                num //= 10
        arr.append([N, num % 10])
    except:
        break

for i, j in arr:
    print(f"{' ' * (4 - len(str(i)))} {i} -> {j}")