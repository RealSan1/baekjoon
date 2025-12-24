import sys
input = sys.stdin.readline

def check(arr, W, LIMIT):
    arr.sort()

    if arr[0] - W / 2 > 0:
        return False

    if arr[-1] + W / 2 < LIMIT:
        return False
    
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > W:
            return False

    return True


while True:
    X, Y, W = map(float, input().split())
    if X == 0 and Y == 0 and W == 0:
        break

    Xarr = list(map(float, input().split()))
    Yarr = list(map(float, input().split()))

    if check(Xarr, W, 75) and check(Yarr, W, 100):
        print("YES")
    else:
        print("NO")