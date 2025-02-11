import sys
input = sys.stdin.readline

N = int(input())

hap = 1
start, end = 1, 1
result = 0

while start <= N:
    if hap < N:
        end += 1
        hap += end

    elif hap > N:
        hap -= start
        start += 1

    elif hap == N:
        result += 1
        hap -= start
        start += 1

print(result)