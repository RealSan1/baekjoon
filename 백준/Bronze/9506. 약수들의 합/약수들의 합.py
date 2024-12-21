while True:
    N = int(input())
    arr = []
    if N == -1:
        break

    for t in range(1, N):
        if N % t == 0: #약수
            arr.append(t)
    if N == sum(arr):
        print(f"{N} = {' + '.join(map(str, arr))}")
    else:
        print(f"{N} is NOT perfect.")