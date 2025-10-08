import sys
input = lambda: sys.stdin.readline().rstrip()

arr = {}
for _ in range(10):
    num = int(input())
    if num in arr:
        arr[num] += 1
    else:
        arr[num] = 1

sort = sorted(arr.items(), key=lambda x: -x[1])
num = sort[0][0]
res = 0
for i in sort:
    res += i[0] * i[1]

print(res//10)
print(num)