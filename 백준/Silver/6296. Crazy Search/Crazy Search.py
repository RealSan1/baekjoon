import sys
input = sys.stdin.readline

N, M = map(int, input().split())
search = input().strip()
result = set()
i = 0
while True:
        temp = search[0+i:N+i]
        if len(temp) != N:
            break
        result.add(temp)
        i += 1

print(len(result))