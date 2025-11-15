import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
res = []

for v in arr:
    A = B = 0
    for i in range(8):
        bit = ((v >> i) & 1) ^ B
        B = bit
        A |= (bit << i)
    res.append(A)

print(*res)