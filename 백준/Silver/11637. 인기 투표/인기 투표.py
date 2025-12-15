import sys
input = lambda: sys.stdin.readline().rstrip()


for _ in range(int(input())):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(int(input()))
    V = arr.copy()
    arr.sort(reverse=True)
    if arr[0] == arr[1]:
        print("no winner")
    elif arr[0] > sum(arr[1:]):
        print(f"majority winner {V.index(arr[0])+1}")
    elif arr[0] <= sum(arr[1:]):
        print(f"minority winner {V.index(arr[0])+1}")
