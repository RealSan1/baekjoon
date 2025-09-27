import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = input()
    if len(N) < 6:
        print(0)
    else:
        s = [chr(i+65) for i in range(26)]
        l = [chr(i+97) for i in range(26)]
        n = [str(i) for i in range(10)]

        num = 6
        i = 0
        res = sys.maxsize
        while True:
            A = N[i:num]
            if any(x in A for x in s) and any(x in A for x in l) and any(x in A for x in n) and len(A) >= 6:
                res = min(res, len(A))
            num += 1
            if num > len(N):
                i += 1
                num = 6

            if i > len(N):
                break


        if res == sys.maxsize:
            print(0)
        else:
            print(res)