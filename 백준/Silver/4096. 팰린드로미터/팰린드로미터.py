import sys
input = sys.stdin.readline

while True:
    N = input().strip()
    if N == '0':
        break
    
    size = len(N)
    N = N.zfill(size)

    reN = N[::-1]
    result = 0
    while N != reN:
        N = int(N)
        N += 1
        result +=1
        N = str(N).zfill(size)
        reN = N[::-1]

    print(result)