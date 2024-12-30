while True:
    try:
        N, K = map(int, input().split())
        치킨 = N
        while N >= K:
            치킨 += N // K
            N = N // K + (N % K)

        print(치킨)
    except:
        break