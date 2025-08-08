import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    res = 0
    for n in range(N):
        V, F, C = map(int, input().split()) # 최고속도, 연료양, 시간당 소비양
        FC = F / C
        num = FC * V
        if num >= D:
            res += 1
    print(res)