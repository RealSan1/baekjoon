import sys
input = sys.stdin.readline

while True:
    try:
        arr = list(map(int, input().split()))
        N = arr[0]
        arr = arr[1:]
        count = [i for i in range(1, N)]        
        for i in range(N-1):
            if abs(arr[i] - arr[i+1]) in count:
                count.remove(abs(arr[i] - arr[i+1]))

        if len(count) == 0:
            print('Jolly')
        else:
            print('Not jolly')
    except:
        break
