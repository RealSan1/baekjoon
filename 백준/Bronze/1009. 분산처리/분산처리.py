import sys
input = sys.stdin.readline

arr = {1: [1], 2: [4, 8, 6, 2], 3: [9, 7, 1, 3], 4: [6, 4], 5: [5], 
       6: [6], 7: [9, 3, 1, 7], 8: [4, 2, 6, 8], 9: [1, 9], 0: [0]}

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    A %= 10
    if A == 0:
        print(10)
    else:
        num = arr[A]
        i = (B - 1) % len(num)
        print(num[i-1])

