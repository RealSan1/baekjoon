N = int(input())
arr = {0:0,
        1:0}
for _ in range(N):
    M = int(input())
    if M == 0:
        arr[0] +=1
    else:
        arr[1] +=1

if arr[0] > arr[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")