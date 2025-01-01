T = int(input())
arr = list(map(int, input().split()))
학생수 = int(input())
for i in range(학생수):
    S, N = map(int, input().split())
    if S == 1: # 남학생
        for i in range(N - 1, len(arr), N): 
            arr[i] = 1 - arr[i]

    else: # 여학생
        N = N-1
        front, back = N, N
        while front >= 0 and back < len(arr) and arr[front] == arr[back]:
                front -= 1
                back += 1
        front += 1
        back -= 1
        
        for i in range(front, back + 1):
            arr[i] = 1 - arr[i]


for i in range(0, len(arr), 20):
    print(" ".join(map(str, arr[i:i + 20])))