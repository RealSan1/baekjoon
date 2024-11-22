N = int(input())
num = list(map(int, input().split()))
temp = num[0]
var = 0
arr = []
for i in range(1, len(num)):
    if temp > num[i]:
        var +=1
    else:
        temp = num[i]
        arr.append(var)
        var = 0
    arr.append(var)
    
print(max(arr))