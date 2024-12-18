import math
M = int(input())
arr = []
for i in range(M):
    case = list(map(int, input().split()))


    for i in range(len(case)):
        for j in range(len(case)):
            if i != j:
                arr.append(math.gcd(case[i], case[j]))
    print(max(arr))
    arr = []