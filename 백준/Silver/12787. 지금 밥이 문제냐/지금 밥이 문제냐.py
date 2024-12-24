N = int(input())
for _ in range(N):
    a, b = map(str, input().split())
    a = int(a)
    if a == 1:
        arr = b.split('.')
        result = ''
        for i in range(len(arr)):
            temp= bin(int(arr[i]))[2:].zfill(8)
            result += temp
        print(int(result, base=2))
    else:
        temp = bin(int(b))[2:]
        temp = '0'*(64-len(temp)) + temp
        print('.'.join([str(int(temp[i:i+8], base=2)) for i in range(0, len(temp), 8)]))