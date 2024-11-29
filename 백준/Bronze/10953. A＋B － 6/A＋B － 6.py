T = int(input())
arr = []
for i in range(T):
    A, B = map(int, input().split(','))
    arr.append(A+B)

for i in range(len(arr)):
    print(arr[i])