import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A = int(input().strip())
    count = 0
    while A != 6174:
        digits = [int(d) for d in str(A).zfill(4)]
        big = int(''.join(map(str, sorted(digits, reverse=True))))
        small = int(''.join(map(str, sorted(digits))))
        A = big - small
        count +=1

    print(count)