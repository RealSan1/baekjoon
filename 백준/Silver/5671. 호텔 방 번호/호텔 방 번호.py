import sys
input = sys.stdin.readline

while True:
    try:
        N, M = map(int, input().split())
        result = 0
        for i in range(N, M+1):
            arr = set()
            for j in str(i):
                arr.add(j)
            if len(arr) == len(str(i)):
                result += 1

        print(result)
    except:
        break
