import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N, K = map(int, input().split())
    candy = list(map(int, input().split()))
    num = 0
    for i in candy:
        if i >= K:
            num += i // K
    print(num)
