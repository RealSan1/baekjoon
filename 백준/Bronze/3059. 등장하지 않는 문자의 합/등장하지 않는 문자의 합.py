import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = set(input().strip())
    hap = 2015
    for i in S:
        hap -= ord(i)
    print(hap)
