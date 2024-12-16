arr = [i for i in range(1, 20+1)]
임시 = []
for i in range(10):
    A, B = map(int, input().split())
    임시 = arr[A-1:B]
    임시.reverse()
    arr[A-1:B] = 임시

print(*arr)