import sys, datetime
input = sys.stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))

cal = datetime.datetime(year=B[0], month=B[1], day=B[2])
cal2 = datetime.datetime(year=A[0], month=A[1], day=A[2])

if B[0] - A[0] > 1000 or (B[0] - A[0] == 1000 and (B[1], B[2]) >= (A[1], A[2])):
    print('gg')
else:
    print(f"D-{(cal - cal2).days}")
