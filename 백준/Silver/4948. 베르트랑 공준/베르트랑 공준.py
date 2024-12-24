while True:
    T = int(input())
    if T == 0:
        break
    start, end = T + 1, 2 * T
    arr = [True] * (end + 1)  
    arr[0], arr[1] = False, False  # 0 1 소수X


    for i in range(2, int(end**0.5) + 1):
        if arr[i]:
            for j in range(i * i, end + 1, i):
                arr[j] = False

    print(sum(arr[start:end + 1]))