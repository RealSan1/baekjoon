import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
num = list(map(int, input().split()))
num.sort()
res = [0] * N
high = int(N/2 + (N % 2))
low = int(high - 1)

for i in range(0, N+2, 2):
    try:
        res[i] = num[low]
        res[i+1] = num[high]
        low -= 1
        high += 1
    except:
        break

print(*res)