import sys
input = sys.stdin.readline

N = int(input())
N = N * (N+1) / 2
print(int((N * 15)+ (N * 20)))