import sys, datetime
input = sys.stdin.readline

N = int(input())
save = [i for i in range(-7, 8)]
for _ in range(N):
    A, B = input().split()
    AM, AD, AY = map(int, A.split('/'))
    BM, BD = map(int, B.split('/'))

    if AM == BM and AD == BD:
        print('SAME DAY')
    else:
        ori = datetime.datetime(AY, AM, AD)
        try:
            T1 = datetime.datetime(AY - 1, BM, BD) # 작년
        except:
            T1 = datetime.datetime(2201, 1, 1)
        try:
            T2 = datetime.datetime(AY, BM, BD) # 올해
        except:
            T2 = datetime.datetime(2201, 1, 1)
        try:
            T3 = datetime.datetime(AY + 1, BM, BD) # 내년            
        except:
            T3 = datetime.datetime(2201, 1, 1)

        for T in [T1, T2, T3]:
            d = (T - ori).days
            if d in save:
                year = T.year
                month = T.month
                day = T.day
                V = "DAY" if abs(d) == 1 else "DAYS"
                fut = "AFTER" if d > 0 else "PRIOR"
                print(f"{month}/{day}/{year} IS {abs(d)} {V} {fut}")
                break
        else:
            print("OUT OF RANGE")