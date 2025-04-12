import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    Alex, Bob = [], []
    result = []
    arr = list(map(int, input().split()))
    for i in arr:
        if i % 2 == 0:
            Bob.append(i)
        else:
            Alex.append(i)
    Bob.sort(reverse=True)
    Alex.sort()
    t, j = 0, 0
    for x in arr:
        if x % 2 == 0:
            result.append(Bob[t])
            t += 1
        else:
            result.append(Alex[j])
            j += 1
    print(f"Case #{_+1}:", *result)