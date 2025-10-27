import sys, math
input = lambda: sys.stdin.readline().rstrip()

MOD = 1000000007
T = int(input())
for t in range(1, T+1):
    M, N = map(int, input().split())
    ans = 0
    for k in range(M+1):
        num = math.comb(M, k) * pow(M-k, N, MOD)
        if k % 2 == 1:
            ans -= num
        else:
            ans += num
        ans %= MOD
    print(f"Case #{t}: {ans % MOD}")