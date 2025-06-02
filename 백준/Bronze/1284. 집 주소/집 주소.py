import sys
input = sys.stdin.readline

while True:
    N = input().strip()
    if N == '0':
        break
    
    count = len(N) + 1
    for i in N:
        if i == '1':
            count += 2
        elif i == '0':
            count += 4
        else:
            count += 3

    print(count)