import sys

arr = dict()
result = ''
for i in range(50):
    try:
        A = list(input())
        
        for i in A:
            if i == ' ':
                continue
            else:
                if i in arr:
                    arr[i] += 1
                else:
                    arr[i] = 1
    except:
        break

sort = sorted(arr.items(), key=lambda x: (-x[1], x[0]))
for key, value in sort:
    if sort[0][1] == value:
        result += key
    else:
        break

print(result)