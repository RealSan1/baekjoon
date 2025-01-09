N = int(input())
arr = list(map(int, input().split()))
find = int(input())

arr.sort()
start, end = 0, len(arr)-1
result = 0
while start < end:

    hap = arr[start] + arr[end]
    if hap == find:
        result += 1
        start += 1
        end -=1

    elif hap > find:
        end -= 1
    
    elif hap < find:
        start += 1


print(result)