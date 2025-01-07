M = int(input())
N = int(input())

arr = []
for i in range(M, N+1):
    if i > 1:
        temp = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                temp = False
                break

        if temp: 
            arr.append(i)
            
if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)