N = int(input())
방무 = 0
T = list(map(int, input().split()))
for i in T:
    방무 = 1 - (1 - 방무) * (1 - (i / 100))
    print(round(방무 * 100, 6))