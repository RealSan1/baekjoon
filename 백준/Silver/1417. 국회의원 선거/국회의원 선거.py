import sys
input = sys.stdin.readline

N = int(input())
ME = int(input())
result = 0
if N > 1:
    arr = []
    for _ in range(N-1):
        arr.append(int(input()))

    while True:
        if max(arr) >= ME:
            temp = max(arr) - 1
            ME += 1
            arr[arr.index(max(arr))] = temp
            result += 1
        else:
            break
    
print(result)