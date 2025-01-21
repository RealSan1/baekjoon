import sys
input = sys.stdin.readline

T = int(input())
arr = []
for _ in range(T):
    A = float(input())
    arr.append(A)

arr.sort()
for i in arr[:7]:
    print(f"{i:.3f}")