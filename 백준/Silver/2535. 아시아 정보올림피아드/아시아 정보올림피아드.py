import sys
input = lambda: sys.stdin.readline().rstrip()

arr = []
N = int(input())
for i in range(N):
    A, B, C = map(int, input().split())
    arr.append([A,B,C])

arr = sorted(arr, key=lambda x: -x[2])
num = 0

if arr[0][0] == arr[1][0] :
    num = 1

print(arr[0][0], arr[0][1])
print(arr[1][0], arr[1][1])
for i in range(2, N):
    if num == 0: 
        print(arr[i][0], arr[i][1])
        break
    else:
        if arr[1][0] != arr[i][0]:
            print(arr[i][0], arr[i][1])
            break

"""
3
1 1 100
1 2 91
1 3 10
"""