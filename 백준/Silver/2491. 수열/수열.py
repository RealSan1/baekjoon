N = int(input())
arr = list(map(int, input().split()))
small = 1
big = 1
result = 1
for i in range(len(arr)-1):
    A, B = arr[i], arr[i+1]
    if A > B : # 오름차순
        big = 1
        small += 1

    elif A == B:
        small += 1
        big += 1

    else : # 내림차순
        small = 1
        big += 1

    result = max(small, big, result)
        

print(result)