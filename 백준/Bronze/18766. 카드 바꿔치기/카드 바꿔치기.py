import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    card1 = list(map(str, input().split()))
    card2 = list(map(str, input().split()))
    card1.sort()
    card2.sort()
    if card1 == card2:
        print("NOT CHEATER")
    else:
        print("CHEATER")