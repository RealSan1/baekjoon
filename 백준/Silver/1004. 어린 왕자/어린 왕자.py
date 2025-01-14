T = int(input())
for _ in range(T):
    x_1, y_1, x_2, y_2 = map(int, input().split()) # 출발점 도착점
    N = int(input()) # 행성 개수
    count = 0
    for A in range(N):
        c_x, c_y, r = map(int, input().split()) # 행성계 중점 반지름
        dis_1 = (x_1 - c_x)**2 + (y_1 - c_y)**2
        dis_2 = (x_2 - c_x)**2 + (y_2 - c_y)**2
        pow_r = r**2

        if pow_r > dis_1 and pow_r > dis_2:
            continue
        elif pow_r > dis_1:
            count +=1
        elif pow_r > dis_2:
            count +=1

    print(count)