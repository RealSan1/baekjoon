import sys
input = sys.stdin.readline

N = int(input())
result = 0.0
for _ in range(N):
    S, A, T, M = map(float, input().split())
    result += S * (1 + 1 / A) * (1 + M / T) / 4

arr = [result]

P = int(input())
for _ in range(P):
    arr.append(float(input()))
arr.sort()

for i in range(len(arr)):
    if arr[i] == result:
        if i/(P+1)>=0.85:
            print('The total score of Younghoon "The God" is {0:.2f}.'.format(result))
        else:
            print('The total score of Younghoon is {0:.2f}.'.format(result))

