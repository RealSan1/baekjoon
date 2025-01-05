import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, M = map(int, input().split())

    AC = list(map(int, input().split()))
    BC = list(map(int, input().split()))
    AC.sort()
    BC.sort()
    result = 0

    for i in AC:
        for j in BC:
            if i > j:
                result +=1

    print(result)