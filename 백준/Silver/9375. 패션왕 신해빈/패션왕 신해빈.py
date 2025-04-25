import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    arr = {}
    for _ in range(N):
        fashion = input().split()
        if fashion[1] in arr:
            arr[fashion[1]] += 1
        else:
            arr[fashion[1]] = 1

    result = 1
    for count in arr.values():
        result *= (count + 1)

    print(result-1)