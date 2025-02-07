import sys, math
input = sys.stdin.readline

N = int(input())
result = math.factorial(N)
result = str(result)
result = result[::-1]

for i in range(len(result)):
    if result[i] == '0':
        continue
    else:
        print(result[i])
        break
