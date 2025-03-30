import sys
input = sys.stdin.readline

while True:
    low, high = 1, 10  
    honest = True

    while True:
        N = int(input())
        if N == 0:
            sys.exit(0)

        response = input().strip()

        if response == "too high":
            if N <= low:
                honest = False
            high = min(high, N - 1)

        elif response == "too low":
            if N >= high:
                honest = False
            low = max(low, N + 1)

        elif response == "right on":
            if not (low <= N <= high):  
                honest = False

            print("Stan may be honest" if honest else "Stan is dishonest")
            break
