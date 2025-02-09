while True:
    try:
        N = int(input())
        dp = [0] * (251)

        dp[0] = (0, 1)
        dp[1] = (0, 1)
        dp[2] = (2, 1)

        for i in range(2, N+1):
            dp[i] = (dp[i-1][1] * 2, sum(dp[i-1]))

    except :
        break

    print(sum(dp[N]))