import sys
input = sys.stdin.readline

N, S = map(str, input().split())
N = int(N)
count = 0
arr = ""
for i in S:
    if i in arr:
        count += 1
    else:
        arr += i

arr = arr + str(count+4)
arr = str(1906 + N) + arr
arr = arr[::-1]
arr = "smupc_" + arr
print(arr)