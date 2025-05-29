import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    arr.sort(reverse=True)
    for i in range(len(arr)-1):
        result += arr[i] - arr[i+1]
    print(result*2)