import sys
input = sys.stdin.readline

T = int(input())
arr = [0] * T
for i in range(T):
    arr[i] = int(input())

arr.sort()
result = sum(arr[:2]) / 2
for i in arr[2:]:
    result =  (result + i) / 2

print(f"{result:5f}")
