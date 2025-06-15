import sys
input = sys.stdin.readline

i = 1
while True:
    A = list(map(int, input().split()))
    if A[0] == 0:
        break
    print(f"Case {i}: Sorting... done!")
    i += 1