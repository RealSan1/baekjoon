import sys
input = sys.stdin.readline

T = int(input())
result = ['ChongChong']
for _ in range(T):
    A, B = map(str, input().split())

    if A in result:
        result.append(B)
    elif B in result:
        result.append(A)

result = set(result)

print(len(result))