# import sys
# input = sys.stdin.readline
while True:
    try:
        A = input()
        B = input()
        result = []
        for i in A:
            if i in B:
                result.append(i)
                B = B.replace(i, '', 1)
        result.sort()
        print(''.join(result))

    except:
        break