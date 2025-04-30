import sys
input = sys.stdin.readline

T, F, S, P, C = map(int, input().split())
TeamA = (T * 6) + (F * 3) + (S * 2) + (P * 1) + (C * 2)
T, F, S, P, C = map(int, input().split())
TeamB = (T * 6) + (F * 3) + (S * 2) + (P * 1) + (C * 2)
print(TeamA, TeamB)