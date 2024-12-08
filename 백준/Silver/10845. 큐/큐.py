T = int(input())
arr = []
aws = []
for t in range(T):
    A = input()
    if 'push' in A:
        arr.append(int(A[5:]))

    elif 'pop' in A:
        if len(arr) == 0:
            aws.append(-1)
        else:
            aws.append(arr[0])
            temp = arr
            arr = temp[1:len(arr)]            

    elif 'size' in A:
        aws.append(len(arr))

    elif 'empty' in A:
        if len(arr) == 0:
            aws.append(1)
        else:
            aws.append(0)

    elif 'front' in A:
        if len(arr) > 0:
            aws.append(arr[0])
        else:
            aws.append(-1)

    elif 'back' in A:
        if len(arr) > 0:
            aws.append(arr[-1])
        else:
            aws.append(-1)

for i in aws:
    print(i)