import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    num = [arr[1]]
    for i in arr[2:]:
        if i != num[-1]:
            num.append(i)
    
    print(*num, "$")