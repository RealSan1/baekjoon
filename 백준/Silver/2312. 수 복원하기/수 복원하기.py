import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    i = 2
    arr = {}
    while True:
        if N == 1:
            break

        elif N % i == 0:
            N = N // i
            if i in arr:
                arr[i] += 1
            else:
                arr[i] = 1
        else:
            i += 1
            
    for key, value in (sorted(arr.items(), key=lambda x: x[0])):
        print(key, value)