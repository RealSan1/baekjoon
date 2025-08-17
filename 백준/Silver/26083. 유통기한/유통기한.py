import sys, datetime
input = lambda: sys.stdin.readline().rstrip()

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_valid_date(y, m, d):
    if not (2000 <= y <= 2099): return False
    if not (1 <= m <= 12): return False
    dim = days_in_month[m]
    if m == 2 and y % 4 == 0: 
        dim = 29
    return 1 <= d <= dim

def cmp_date(today, exp):
    return today <= exp

Y, M, D = map(int, input().split())
today = (2000+Y, M, D)

N = int(input())
for _ in range(N):
    A, B, C = map(int, input().split())

    candidates = []
    # 연/월/일
    if is_valid_date(2000+A, B, C):
        candidates.append((2000+A, B, C))
    # 일/월/연
    if is_valid_date(2000+C, B, A):
        candidates.append((2000+C, B, A))
    # 월/일/연
    if is_valid_date(2000+C, A, B):
        candidates.append((2000+C, A, B))

    if not candidates:
        print("invalid")
        continue

    if all(cmp_date(today, exp) for exp in candidates):
        print("safe")
    else:
        print("unsafe")