import sys
input = lambda: sys.stdin.readline().rstrip()

arr = []
for H in range(1, 151):
    for W in range(H + 1, 151):
        arr.append(((H*H + W*W), H, W))

arr.sort()

while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    res = ((H*H + W*W), H, W)
    num = arr.index(res)
    sqrt, rH, rW = arr[num+1]
    print(rH, rW)