N = int(input())

for _ in range(N):
    R, E, C = map(int, input().split())
    # 광고 X 수입 / 광고 O 수입 / 광고 비용
    if E - C > R:
        print('advertise')
    elif E - C == R:
        print('does not matter')
    elif E - C < R:
        print('do not advertise')
