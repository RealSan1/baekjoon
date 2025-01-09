N = int(input())
M = int(input())
arr = list(map(int, input().split()))

arr.sort()
start, end = 0, len(arr)-1
result = 0
while start < end:
    hap = arr[start] + arr[end]
    if hap == M:
        result +=1
        start +=1
        end -=1
    elif hap > M:
        end -= 1
    else:
        start += 1

print(result)