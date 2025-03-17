import sys, itertools
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))[1:]
    if len(arr) == 0:
        break

    result = list(itertools.combinations(arr, 6))

    for i in result:
        print(*i)
    print()