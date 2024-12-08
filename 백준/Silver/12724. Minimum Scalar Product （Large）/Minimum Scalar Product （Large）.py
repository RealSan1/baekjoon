T = int(input())
var = 0
for t in range(T):
    n = int(input())
    V1 = list(map(int, input().split()))
    V1.sort(reverse=True)
    V2 = list(map(int, input().split()))
    V2.sort()
    for i in range(len(V1)):
        var += V1[i] * V2[i]
    print(f"Case #{t+1}: {var}")
    var = 0