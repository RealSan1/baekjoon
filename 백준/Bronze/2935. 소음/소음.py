arr = []
for i in range(3):
    A = input()
    arr.append(A)

if arr[1] == '+':
    print(int(arr[0]) + int(arr[2]))
else:
    print(int(arr[0]) * int(arr[2]))
