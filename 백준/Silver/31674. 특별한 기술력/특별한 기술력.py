import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7
n = int(input())
heights = list(map(int, input().split()))

heights.sort(reverse=True)
total_sum = 0

for height in heights:
    total_sum = (total_sum + total_sum + height) % MOD
print(total_sum)