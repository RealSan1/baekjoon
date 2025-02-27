import sys
input = sys.stdin.readline

T = int(input())
arr = {}
result = 0
for _ in range(T):
    name = input().strip()
    K, M = map(int, input().split())
    temp = 0
    while M >= K:
        M = M - K + 2
        temp += 1
    result += temp
    arr[name] = temp

print(result)
for key,value in arr.items():
    if max(arr.values()) == value:
        print(key)
        break