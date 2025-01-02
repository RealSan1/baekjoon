T = int(input())
for _ in range(T):
    A = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    temp = [] # 할인가
    i = 0
    while True:
        if len(temp) == A:
            break
        
        R = int(arr[i] * 0.75)
        if R in arr:
            temp.append(R)
            arr.pop(i)
            arr.remove(R)
            i = 0
        else:
            i += 1

    temp.reverse()
    print(f"Case #{_+1}: {' '.join(map(str, temp))}")

"""
1
2
27 36 48 64

27 48
"""